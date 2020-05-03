from ..abstract import AbstractFilter

class BaseUnicodeFilter(AbstractFilter):
    """Filters strings to ASCII/Unicode."""

    NAME = "BaseUnicode_DoNotExpose"
    
    def __init__(self):
        pass

    def filter_line_switchable(self, line, return_ascii_only=True):
        """Filter a single line of data."""
        is_unicode = True
        try:
            line.decode("ascii")
        except UnicodeDecodeError:
            is_unicode = False

        if return_ascii_only:
            if is_unicode:
                return ""
            else:
                return line
        else:
            if is_unicode:
                return line
            else:
                return ""


class UnicodeFilter(BaseUnicodeFilter):

    NAME = "unicodeOnly"

    def info(self):
        """Display information about this filter."""
        return """UnicodeFilter

        Returns lines that do not only contain ASCII characters.
        Useful for filtering on foreign character sets or corrupt data."""

    def filter_line(self, line):
        return self.filter_line_switchable(line, False)


class AsciiFilter(BaseUnicodeFilter):

    NAME = "asciiOnly"

    def info(self):
        """Display information about this filter."""
        return """AsciiFilter

        Returns lines that are only ASCII characters."""

    def filter_line(self, line):
        return self.filter_line_switchable(line, True)
