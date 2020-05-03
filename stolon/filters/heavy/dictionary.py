from ..abstract import AbstractFilter
from ...util.config import Config

import glob
import gzip
import logging
import os

logger = logging.getLogger("validators.DictionaryValidator")


class DictionaryFilter(AbstractFilter):

    CASE_SENSITIVE = True
    NAME = "dictionary"
    supported_langs = {}
    wordlist_dir = None

    _dictionary_hash = {}

    def __init__(self):
        """Initialises dictionaries used by the validator."""

        logger.debug("Getting wordlists")
        self.wordlist_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../../wordlists/')
        )
        
        self.supported_langs = self._get_supported_langs()
        for lang in Config.lang:
            self._load_language(lang)

    def info(self):
        return """Dictionary Filter

        Filters lines that are not found in Stolon's in-built dictionaries.
        For Chinese, will check against both Chinese characters as well as Pinyin."""


    def filter_line(self, line):
        """Checks the in-memory dictionary whether the word exists."""
        line = line.strip().lower()
        if line in self._dictionary_hash:
            return line
        
        return ""


    def _get_supported_langs(self):
        """Get a list of supported langs from wordlists."""
        logger.debug("Loading supported languages")
        langs = {}
        files = glob.glob(os.path.join(self.wordlist_dir, "*.gz"))
        for file in files:
            # get the extension
            filename = os.path.basename(file).split(".")
            lang = filename[0]
            if len(lang) == 2:
                logger.debug("Wordlist file %s supports lang '%s'" % (file, lang))
                if lang not in langs:
                    langs[lang] = []
                langs[lang].append(file)
        return langs

    
    def _load_language(self, lang):
        """Load a language from the file."""
        if lang not in self.supported_langs:
            raise IOError("Attempting to load language files for unsupported lang %s" % lang)

        for file in self.supported_langs[lang]:
            logger.debug("Loading dictionary from file %s" % file)
            items = 0
            with gzip.open(file, mode="r") as gzfd:
                for line in gzfd:
                    items += 1
                    word = line.strip()
                    if not self.CASE_SENSITIVE:
                        if all(ord(char) < 128 for char in word):
                            # only lowercase ascii chars
                            word = word.lower()
                    # let's make a bastard use of dictionary
                    # to create fast lookups
                    self._dictionary_hash[word] = 1
            logger.debug("Done, loaded %d items" % items)
                    



