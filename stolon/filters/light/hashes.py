from ..abstract import AbstractFilter
import re

class HashFilter(AbstractFilter):
    """Filters strings that contain hashes."""

    NAME = "hash"
    hash_regexes = []

    def __init__(self):
        self.hash_regexes = [
            re.compile(r'(^|[^a-fA-F0-9])[a-fA-F0-9]{32}([^a-fA-F0-9]|\$)'),
            re.compile(r'[0-7][0-9a-f]{7}[0-7][0-9a-f]{7}'),
            re.compile(r'([0-9a-zA-Z]{32}):(\w{32})'),
            re.compile(r'([0-9a-zA-Z]{32}):(\S{3,32})'),
            re.compile(r'\$H\$\S{31}'),
            re.compile(r'\$P\$\S{31}'),
            re.compile(r'\$S\$\S{52}'),
            re.compile(r'\$1\$\w{8}\S{22}'),
            re.compile(r'\$6\$\w{8}\S{86}'),
            re.compile(r'(^|[^a-fA-F0-9])[a-fA-F0-9]{40}([^a-fA-F0-9]|$)'),
            re.compile(r'(^|[^a-fA-F0-9])[a-fA-F0-9]{128}([^a-fA-F0-9]|$)'),
            re.compile(r'(^|[^a-fA-F0-9])[a-fA-F0-9]{64}([^a-fA-F0-9]|$)'),
            re.compile(r'(^|[^a-fA-F0-9])[a-fA-F0-9]{96}([^a-fA-F0-9]|$)'),
            re.compile(r'\$2a\$10\$\S{53}'),
            re.compile(r'\$apr1\$\w{8}\S{22}'),
            re.compile(r'\$md5\$rounds\=904\$\w{16}\S{23}'),
            re.compile(r'\$5\$\w{8}\$\S{43}'),
            re.compile(r'\{ssha256\}06\$\S{16}\$\S{43}'),
            re.compile(r'\{ssha1\}06\$\S{16}\$\S{27}'),
            re.compile(r'\$ml\$\w{5}\$\w{64}\$\w{128}'),
            re.compile(r'([0-9a-fA-F]{130}):(\w{40})'),
            re.compile(r'\$8\$\S{14}\$\S{43}'),
            re.compile(r'\$9\$\S{14}\$\S{43}'),
            re.compile(r'pbkdf2_sha256\$20000\$\S{57}'),
            re.compile(r'sha1\$\w{5}\$\w{40}'),
            re.compile(r'(0x\w{52})'),
            re.compile(r'(0x\w{92})'),
            re.compile(r'([0-9]{1,3}[\.]){3}[0-9]{1,3}')
        ]

    def info(self):
        """Display information about this filter."""
        return """HashFilter

        Filters lines that contain things that look like known hashes. Hash regexes
        for this filter have been taken from Rurasort:

        https://github.com/bitcrackcyber/rurasort"""

    def filter_line(self, line):
        """Filter a single line of data."""
        found_hash = True
        for regex in self.hash_regexes:
            result = hash_re.search(inputstring)
            if result:
                found_hash = True
                break
        if found_hash:
            return ""
        return line
