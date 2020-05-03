from ..abstract import AbstractFilter
from bs4 import BeautifulSoup

class HTMLFilter(AbstractFilter):
    """Takes HTML and returns words."""

    NAME = "html"

    def __init__(self):
        pass

    def info(self):
        """Display information about this filter."""
        return """HTML Filter

        Uses BeautifulSoup4 to remove all HTML tags, leaving only words that
        existed as Text content. Useful for scraping words out of HTML results with lines.
        """

    def filter_line(self, line):
        """Filter a single line of data."""

        parsed = ''.join(BeautifulSoup(line, "html.parser").findAll(text=True))
        words = parsed.lower().split()
        wordstr = ""
        for word in words:
            wordstr += "%s\n" % word.lstrip().rstrip().encode('iso-8859-1')
        return words

class WebpageFilter(AbstractFilter):
    """Takes HTML and returns words."""

    NAME = "webpage"

    def __init__(self):
        pass

    def info(self):
        """Display information about this filter."""
        return """Webpage Filter

        Eats an entire page of content and distills wordlike things from it.
        """

    def filter_line(self, page):
        """Filter a single line of data. Or in this case, everything."""
        parsed = BeautifulSoup(page, "html.parser").findAll(text=True)
        wordstr = ""
        for word in parsed:
            wordstr += "%s\n" % word.lstrip().rstrip()
        return wordstr