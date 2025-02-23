class LexerError(Exception):
    """Base lexer error"""

class UnexpectedSymbolError(LexerError):
    """Unexpected symbol error"""
