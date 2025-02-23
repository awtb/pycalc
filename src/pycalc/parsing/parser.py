from typing import List

from pycalc.exceptions.parser import UnexpectedTokenError, EOF
from pycalc.lexing.types import Token, TokenType
from pycalc.parsing.types import (
    OperationType,
    Instruction,
    BinaryOperation,
    ConstantInstruction,
    ConstantType,
    IdentifierInstruction,
    UnaryOperation,
)


class Parser:
    def __init__(self, tokens: List[Token]):
        self._tokens = tokens
        self._pos = 0

    def _consume_token(self) -> Token:
        token = self._tokens[self._pos]
        self._pos += 1
        return token

    def _current_token(self) -> Token:
        try:
            return self._tokens[self._pos]
        except IndexError:
            return self._tokens[-1]  # EOF

    def _parse_leaf(self) -> Instruction:
        tok = self._consume_token()

        if tok.type == TokenType.FLOAT:
            return ConstantInstruction(tok.value, ConstantType.FLOAT)
        elif tok.type == TokenType.INT:
            return ConstantInstruction(tok.value, ConstantType.INT)
        elif tok.type == TokenType.IDENT:
            return IdentifierInstruction(tok.value)

        raise UnexpectedTokenError(
            f"Expected constant or identifier found {tok.type}, line {tok.lineno} ch: {tok.character}",
        )

    def _parse_zero_priority_expression(self) -> Instruction:
        tok = self._current_token()

        if tok.type == TokenType.EOF:
            raise UnexpectedTokenError(
                f"Expected '(', identifier or constant, found {tok.type}"
            )

        if tok.type != TokenType.LPAREN:
            return self._parse_leaf()

        self._consume_token()
        expr = self._parse_instruction()
        self._expect_token(TokenType.RPAREN)

        return expr

    def _parse_unary_operation(self) -> Instruction:
        current_token = self._current_token()

        if current_token.type == TokenType.EOF:
            raise EOF(
                f"Expected expression, constant or literal, found EOF, line {current_token.lineno} ch: {current_token.character}",
            )

        if current_token.type == TokenType.MINUS:
            self._consume_token()
            return UnaryOperation(
                OperationType.SUBTRACTION, self._parse_unary_operation()
            )

        return self._parse_zero_priority_expression()

    def _expect_token(self, token_type: TokenType):
        consumed = self._consume_token()

        if consumed.type != token_type:
            raise UnexpectedTokenError(
                f"Unexpected token, expected token {token_type}, found {consumed.type}"
            )

        return consumed

    def _parse_high_priority_binary_operation(self) -> Instruction:
        expression = self._parse_unary_operation()
        current_token = self._current_token()

        while current_token.type != TokenType.EOF:
            current_token = self._current_token()

            if current_token.type == TokenType.MUL:
                op_type = OperationType.MULTIPLICATION
            elif current_token.type == TokenType.DIV:
                op_type = OperationType.DIVISION
            elif current_token.type == TokenType.POW:
                op_type = OperationType.POW
            else:
                break

            self._consume_token()

            expression = BinaryOperation(
                op_type=op_type,
                left=expression,
                right=self._parse_unary_operation(),
            )

            current_token = self._current_token()

        return expression

    def _parse_low_priority_binary_operation(self) -> Instruction:
        expression = self._parse_high_priority_binary_operation()
        current_token = self._current_token()

        while current_token.type != TokenType.EOF:
            if current_token.type == TokenType.PLUS:
                op_type = OperationType.ADDITION

            elif current_token.type == TokenType.MINUS:
                op_type = OperationType.SUBTRACTION
            else:
                break

            self._consume_token()

            expression = BinaryOperation(
                op_type=op_type,
                left=expression,
                right=self._parse_high_priority_binary_operation(),
            )

            current_token = self._current_token()

        return expression

    def _parse_instruction(self) -> Instruction:
        return self._parse_low_priority_binary_operation()

    def parse(self) -> List[Instruction]:
        instructions_list = []

        while (
            self._pos < len(self._tokens)
            and self._current_token().type != TokenType.EOF
        ):
            instructions_list.append(self._parse_instruction())

        return instructions_list
