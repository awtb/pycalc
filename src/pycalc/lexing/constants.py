from src.pycalc.lexing.types import TokenType

CHARS_TOKEN_MAPPING = {
    '*': TokenType.MUL,
    '+': TokenType.PLUS,
    '-': TokenType.MINUS,
    '/': TokenType.DIV,
    '(': TokenType.LPAREN,
    ')': TokenType.RPAREN,
}