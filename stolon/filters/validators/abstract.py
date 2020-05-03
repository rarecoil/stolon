from ..abstract import AbstractFilter

class AbstractValidator(AbstractFilter):
    """Abstract validator"""

    NAME = "abstract"

    def __init__(self):
        pass

    def filter_line(self, line):
        """Use a validator as a boolean filter."""
        if self.validate(line) > 0.5:
            return line
        return ""

    def validate(self, candidate_word):
        """Attempts to validate a word based upon something that exists. Returns a score between 0-1."""
        raise NotImplementedError("validate has not been implemented, please implement the validate method")

    def pass_validation_above(self, candidate_word, weight=0.5):
        """Pass validation above or equal to a given threshold. Useful when using fuzzier classifiers."""
        return self.validate(candidate_word) >= weight
    