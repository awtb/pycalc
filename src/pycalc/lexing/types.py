from enum import Enum


class TokenType(Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"


class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"{self.type}: {self.value}"
