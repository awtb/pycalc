from typing import List

from src.pycalc.lexing.constants import CHARS_TOKEN_MAPPING
from src.pycalc.lexing.types import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = text
        self._pos = 0
        self._result = []

    def _parse_literal(self) -> Token:
        value = ""
        tok_type = TokenType.INT

        while self._pos < len(self.text):
            if self.text[self._pos] == ".":
                tok_type = TokenType.FLOAT
            elif not self.text[self._pos].isdigit():
                break

            value += self.text[self._pos]
            self._pos += 1

        return Token(tok_type, value)

    def _parse_name(self) -> Token:
        value = ""
        tok_type = TokenType.IDENT

        while self._pos < len(self.text):
            if not self.text[self._pos].isalpha() and not self.text[self._pos].isdigit():
                break

            value += self.text[self._pos]
            self._pos += 1

        return Token(tok_type, value)

    def tokenize(self) -> List[Token]:
        while self._pos < len(self.text):
            if self.text[self._pos] in CHARS_TOKEN_MAPPING:
                self._result.append(
                    Token(
                        CHARS_TOKEN_MAPPING[self.text[self._pos]],
                        self.text[self._pos],
                    )
                )
                self._pos += 1
            elif self.text[self._pos].isdigit():
                self._result.append(
                    self._parse_literal()
                )
                continue

            elif self.text[self._pos].isalpha():
                self._result.append(
                    self._parse_name(),
                )
            elif self.text[self._pos].isspace():
                self._pos += 1

        return self._result
