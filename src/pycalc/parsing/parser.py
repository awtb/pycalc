from typing import List

from pycalc.lexing.types import Token, TokenType
from pycalc.parsing.types import OperationType, Instruction, BinaryOperation, ConstantInstruction, ConstantType, \
    IdentifierInstruction, UnaryOperation


class Parser:
    def __init__(self, tokens: List[Token]):
        self._tokens = tokens
        self._pos = 0

    def _consume_token(self) -> Token:
        token = self._tokens[self._pos]
        self._pos += 1
        return token

    def _has_next(self) -> bool:
        return self._pos >= len(self._tokens)

    def _next_token(self) -> Token:
        token = self._tokens[self._pos + 1]
        return token

    def _current_token(self) -> Token | None:
        try:
            return self._tokens[self._pos]
        except IndexError:
            return None

    def _parse_op_type(self) -> OperationType:
        tok = self._consume_token()

        if tok.type == TokenType.MUL:
            return OperationType.MULTIPLICATION
        elif tok.type == TokenType.DIV:
            return OperationType.DIVISION
        elif tok.type == TokenType.PLUS:
            return OperationType.ADDITION
        elif tok.type == TokenType.MINUS:
            return OperationType.SUBTRACTION

        raise RuntimeError("Unexpected token", tok)

    def _parse_leaf(self) -> Instruction:
        tok = self._consume_token()

        if tok.type == TokenType.FLOAT:
            return ConstantInstruction(tok.value, ConstantType.FLOAT)
        elif tok.type == TokenType.INT:
            return ConstantInstruction(tok.value, ConstantType.INT)
        elif tok.type == TokenType.IDENT:
            return IdentifierInstruction(tok.value)

        raise RuntimeError("Unexpected token", tok)

    def _parse_unary_operation(self) -> Instruction:
        current_token = self._current_token()

        if current_token.type == TokenType.PLUS:
            op_type = OperationType.ADDITION
        elif current_token.type == TokenType.MINUS:
            op_type = OperationType.SUBTRACTION
        else:
            return self._parse_leaf()

        self._consume_token()

        return UnaryOperation(op_type, self._parse_instruction())

    def _expect_token(self, token_type: TokenType):
        consumed = self._consume_token()

        if consumed.type != token_type:
            raise RuntimeError("Unexpected token", consumed)

        return consumed

    def _next_type(self) -> TokenType | None:
        if (self._pos + 1) < len(self._tokens):
            return self._tokens[self._pos + 1].type

    def _parse_high_priority_binary_operation(self) -> Instruction:
        expression = self._parse_unary_operation()

        while True:
            current_token = self._current_token()

            if current_token is None:
                break

            if current_token.type == TokenType.MUL:
                op_type = OperationType.MULTIPLICATION

            elif current_token.type == TokenType.DIV:
                op_type = OperationType.DIVISION
            else:
                break

            self._consume_token()

            expression = BinaryOperation(
                op_type=op_type,
                left=expression,
                right=self._parse_unary_operation(),
            )

        return expression

    def _parse_low_priority_binary_operation(self) -> Instruction:
        expression = self._parse_high_priority_binary_operation()

        while True:
            current_token = self._current_token()

            if current_token is None:
                break

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

        return expression

    def _parse_instruction(self) -> Instruction:
        return self._parse_low_priority_binary_operation()

    def parse(self) -> Instruction:
        return self._parse_instruction()
