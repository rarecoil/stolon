class AbstractFilter(object):
    """AbstractFilter, the core inherited variant of filter."""

    NAME = "abstract"

    def __init__(self):
        pass

    def info(self):
        """Display information about this filter."""
        raise NotImplementedError("AbstractFilter does not implement info. Please implement info.")

    def filter_line(self, line):
        """Filter a single line of data."""
        raise NotImplementedError("AbstractFilter cannot filter data! Please implement FilterLine.")