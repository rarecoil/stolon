from ..abstract import AbstractFilter

class WhitespaceFilter(object):
    """WhitespaceFilter, the core inherited variant of filter."""

    NAME = "whitespace"

    def __init__(self):
        pass

    def info(self):
        """Display information about this filter."""
        return """WhitespaceFilter

        Filters lines that only contain whitespace."""

    def filter_line(self, line):
        """Filter a single line of data."""
        
        line = line.strip()
        return line