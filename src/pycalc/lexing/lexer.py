from typing import Callable, List

from pycalc.exceptions.lexer import UnexpectedSymbolError
from src.pycalc.lexing.constants import CHARS_TOKEN_MAPPING
from src.pycalc.lexing.types import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = text
        self._pos = 0
        self._lineno = 0
        self._result = []

    def _parse_till(self, fn: Callable[[str], bool]):
        value = ""

        while self._pos < len(self.text) and fn(self.text[self._pos]):
            value += self.text[self._pos]
            self._pos += 1

        return value

    def _parse_literal(self) -> Token:
        """
        Parses a constant expressions like `123` or `12.1`
        :return:
        """
        value = ""
        tok_type = TokenType.INT

        while self._pos < len(self.text):
            if self.text[self._pos] == ".":
                tok_type = TokenType.FLOAT
            elif not self.text[self._pos].isdigit():
                break

            value += self.text[self._pos]
            self._pos += 1

        return self._build_token(tok_type, value)

    def _parse_identifier(self) -> Token:
        """
        Parses an identifier
        :return:
        """
        value = ""
        tok_type = TokenType.IDENT

        while self._pos < len(self.text):
            if (
                not self.text[self._pos].isalpha()
                and not self.text[self._pos].isdigit()
            ):
                break

            value += self.text[self._pos]
            self._pos += 1

        return self._build_token(tok_type, value)

    def _build_token(
        self,
        token_type: TokenType,
        value: str,
    ):
        return Token(token_type, value, self._lineno, self._pos)

    def _unexpected_symbol(self, symbol: str):
        raise UnexpectedSymbolError(
            "Unexpected {} Line: {}, Ch: {}".format(
                self.text[self._pos],
                self._lineno,
                self._pos,
            )
        )

    def tokenize(self) -> List[Token]:
        """
        Tokenize the text into a list of Token objects.
        :return:
        """
        while self._pos < len(self.text):
            if self.text[self._pos] in CHARS_TOKEN_MAPPING:
                self._result.append(
                    self._build_token(
                        CHARS_TOKEN_MAPPING[self.text[self._pos]],
                        self.text[self._pos],
                    )
                )
                self._pos += 1
            elif self.text[self._pos].isdigit():
                self._result.append(self._parse_literal())
            elif self.text[self._pos] == ",":
                self._result.append(
                    self._build_token(TokenType.COMMA, self.text[self._pos])
                )
                self._pos += 1
            elif self.text[self._pos].isalpha():
                self._result.append(
                    self._parse_identifier(),
                )
            elif self.text[self._pos].isspace():
                self._pos += 1
            elif self.text[self._pos] == "\n":
                self._pos += 1
                self._lineno += 1
            else:
                self._unexpected_symbol(self.text[self._pos])

        self._result.append(self._build_token(TokenType.EOF, value="EOF"))

        return self._result
