from enum import StrEnum


class TokenType(StrEnum):
    INT = "INT"
    FLOAT = "FLOAT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    IDENT = "NAME"
    POW = "POW"
    EOF = "EOF"


class Token:
    def __init__(self, token_type: TokenType, value: str, lineno: int, character: int):
        self.type = token_type
        self.value = value
        self.lineno = lineno
        self.character = character

    def __str__(self):
        return f"{self.type}: {self.value}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.type}, {self.value})"
