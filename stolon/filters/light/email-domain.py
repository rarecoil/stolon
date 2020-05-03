from ..abstract import AbstractFilter
import re

class EmailDomainFilter(AbstractFilter):
    """Filters domains from email addresses."""

    NAME = "email"
    EMAIL_RE_STRING = r"^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    regex = None

    def __init__(self):
        self.regex = re.compile(self.EMAIL_RE_STRING)

    def info(self):
        """Display information about this filter."""
        return """EmailDomainFilter

        Includes only lines that appear to be domains from email addresses."""

    def filter_line(self, line):
        """Filter a single line of data."""
        
        if self.regex.search(line):
            return line
        return ""
