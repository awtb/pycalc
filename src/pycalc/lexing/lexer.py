from typing import List

from src.pycalc.lexing.types import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = text
        self._pos = 0

    def _get_value(self):
        value = ""
        tok_type = TokenType.INT

        while self._pos < len(self.text):
            if self.text[self._pos] == ".":
                tok_type = TokenType.FLOAT
            if not self.text[self._pos].isdigit():
                break

            value += self.text[self._pos]
            self._pos += 1

        return Token(tok_type, value)

    def tokenize(self) -> List[Token]:
        result = []

        while self._pos < len(self.text):

            if self.text[self._pos] == "*":
                result.append(Token(TokenType.MUL, "*"))
            if self.text[self._pos] == "-":
                result.append(Token(TokenType.MINUS, self.text[self._pos]))
            elif self.text[self._pos] == '(':
                result.append(Token(TokenType.LPAREN, '('))
            elif self.text[self._pos] == ')':
                result.append(Token(TokenType.RPAREN, ')'))

            elif self.text[self._pos].isdigit():
                result.append(
                    self._get_value()
                )
                continue

            self._pos += 1


        return result
