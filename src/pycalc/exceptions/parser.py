class ParserError(Exception):
    """Parser error"""


class UnexpectedTokenError(ParserError):
    """Unexpected token error"""


class EOF(ParserError):
    """EOF"""
