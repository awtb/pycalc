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
    COMMA = "COMMA"


class Token:
    def __init__(
        self,
        token_type: TokenType,
        value: str,
        lineno: int,
        character: int,
    ) -> None:
        self.type = token_type
        self.value = value
        self.lineno = lineno
        self.character = character

    def __str__(self) -> str:
        return f"{self.type}: {self.value}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[{self.type}, {self.value}]"
