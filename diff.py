"""Module that defines the Diff class"""

class Diff:
    """A hashable class that represents a git Diff."""

    diff_string : str
    diff_hash: int
    positions: (int, int)

    def __init__(self, diff_string : str):
        # Only shows upto the last fours lines
        diff_as_lines = diff_string.splitlines()
        self.diff_string = "\n".join(diff_as_lines[-4:])
        # This is the position of the final file. If the file was modified and
        # the review comment was left at the original location, the line number
        # at the GitHub UI and this would be different.
        end_position = len(diff_as_lines) - 1
        start_position = end_position - 3 if end_position > 3 else 1
        self.positions = (start_position, end_position)
        self.diff_hash = hash(self.diff_string)

    def __eq__(self, other):
        return self.diff_hash == other.diff_hash

    def __hash__(self):
        return self.diff_hash
