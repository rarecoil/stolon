from ..abstract import AbstractFilter

from spellchecker import SpellChecker

class SpellcheckFilter(AbstractFilter):
    """Uses PySpellChecker in order to attempt to create spellchecked candidates."""

    NAME = "spellcheck"
    spellchecker = None

    def __init__(self):
        self.spellchecker = SpellChecker()

    def info(self):
        """Display information about this filter."""
        return """Spellcheck Filter

        Takes a candidate line and feeds it into PySpellChecker (https://pypi.org/project/pyspellchecker/)
        in an attempt to generate potential word candidates based upon Levenshtein distance.
        This is similar to wordlist expansion done by iphelix's PACK.
        """

    def filter_line(self, line):
        """Filter a single line of data."""

        misspelled = self.spellchecker.unknown(line)

        candidates = []
        for word in misspelled:
            candidates.append(self.spellchecker.candidates(word))
        return candidates