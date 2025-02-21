from typing import List

from pycalc.lexing.types import Token, TokenType
from pycalc.parsing.types import OperationType, Instruction, BinaryOperation, Constant, ConstantType, \
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

    def _current_token(self) -> Token:
        return self._tokens[self._pos]

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
            return Constant(tok.value, ConstantType.FLOAT)
        elif tok.type == TokenType.INT:
            return Constant(tok.value, ConstantType.INT)
        elif tok.type == TokenType.IDENT:
            return IdentifierInstruction(tok.value)

        raise RuntimeError("Unexpected token", tok)

    def _token_type_to_op_type(self, token_type: TokenType) -> OperationType:
        if token_type == TokenType.MUL:
            return OperationType.MULTIPLICATION
        elif token_type == TokenType.DIV:
            return OperationType.DIVISION
        elif token_type == TokenType.PLUS:
            return OperationType.ADDITION
        elif token_type == TokenType.MINUS:
            return OperationType.SUBTRACTION

        raise RuntimeError("Unexpected token", token_type)

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

    def _parse_binary_operation(self) -> Instruction:
        first_expr = self._parse_unary_operation()

        if self._pos >= len(self._tokens):
            return first_expr

        current_token = self._current_token()

        if current_token.type == TokenType.PLUS:
            op_type = OperationType.ADDITION
        elif current_token.type == TokenType.MINUS:
            op_type = OperationType.SUBTRACTION
        elif current_token.type == TokenType.MUL:
            op_type = OperationType.MULTIPLICATION
            self._consume_token()
            return BinaryOperation(self._parse_instruction(), first_expr, op_type)
        elif current_token.type == TokenType.DIV:
            op_type = OperationType.DIVISION
            self._consume_token()
            return BinaryOperation(self._parse_instruction(), first_expr, op_type)
        else:
            # If there's no approaches to parse binary operation (there's no other ops)
            # Just return first expression and continue parsing.
            return first_expr

        self._consume_token()

        return BinaryOperation(first_expr, self._parse_instruction(), op_type)

    def _parse_instruction(self) -> Instruction:
        # Let's try to parse binop

        return self._parse_binary_operation()
