from ..util.registry import FilterRegistry

from .heavy.nltk import NltkPorterStemmer
from .heavy.leetspeak import LeetspeakFilter
from .heavy.spellcheck import SpellcheckFilter
from .heavy.html import HTMLFilter, WebpageFilter
FilterRegistry.add(NltkPorterStemmer)
FilterRegistry.add(LeetspeakFilter)
FilterRegistry.add(SpellcheckFilter)
FilterRegistry.add(HTMLFilter)
FilterRegistry.add(WebpageFilter)

from .light.email import EmailFilter
from .light.hashes import HashFilter
from .light.unicode import UnicodeFilter, AsciiFilter
from .light.whitespace import WhitespaceFilter
FilterRegistry.add(EmailFilter)
FilterRegistry.add(HashFilter)
FilterRegistry.add(UnicodeFilter)
FilterRegistry.add(AsciiFilter)
FilterRegistry.add(WhitespaceFilter)

from .heavy.dictionary import DictionaryFilter
FilterRegistry.add(DictionaryFilter)