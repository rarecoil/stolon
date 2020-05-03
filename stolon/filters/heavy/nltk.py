from ..abstract import AbstractFilter

from nltk.stem import PorterStemmer

class NltkPorterStemmer(AbstractFilter):
    """NLTK Porter Stemmer."""

    NAME = "porter"
    stemmer = None

    def __init__(self):
        self.stemmer = PorterStemmer()

    def info(self):
        """Display information about this filter."""
        return """NltkPorterStemmer

        Uses the Python NLTK library's Porter Stemmer (https://www.nltk.org/howto/stem.html)
        in an attempt to generate a stem from a given word."""

    def filter_line(self, line):
        """Filter a single line of data."""
        
        line = line.strip()
        stem = self.stemmer.stem(line)
        if len(stem):
            return stem

        return ""