from ..abstract import AbstractFilter

from itertools import combinations

class LeetspeakFilter(AbstractFilter):
    """Leetspeak bruteforce filter"""

    NAME = "leetspeak"
    LEETSPEAK_SUBSTITUTIONS = [
        ("4", "a"),
        ("3", "e"),
        ("1", "i"),
        ("1", "l"),
        ("7", "t"),
        ("6", "b"),
        ("0", "o"),
        ("&", "and"),
        ("&", "anned")
    ]

    def __init__(self):
        pass

    def info(self):
        """Display information about this filter."""
        return """Leetspeak Bruteforce Filter

        Generates multiple 1337speak word candidates and expands the
        wordlist to potential ASCII substitutions. This grows relatively
        large with the number of potential substitutions.
        
        For stemming, this is useful when combined with the dictionary filter."""

    def filter_line(self, line):
        """Filter a single line of data."""
        candidates = []

        leetspeak_substitute_combos = combinations(self.LEETSPEAK_SUBSTITUTIONS)
        for substitution_list in leetspeak_substitute_combos:
            tmp = line
            for substitution in substitution_list:
                tmp = tmp.replace(substitution[0], substitution[1])
            candidates.add(tmp)

        return candidates


