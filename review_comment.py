"""A module that exports the class ReviewComment"""

class ReviewComment:
    """A class that represents a GitHub review comment."""

    author: str
    body: str
    url: str

    def __init__(self, author, body, url):
        self.author = author
        self.body = body.replace("\r\n", "\n")
        self.url = url
