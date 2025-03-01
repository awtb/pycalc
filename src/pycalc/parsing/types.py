from abc import ABC
from enum import Enum
from typing import List


class OperationType(Enum):
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4
    EQUAL = 5
    NOT_EQUAL = 6
    POW = 7


class ConstantType(Enum):
    INT = 1
    FLOAT = 2


class Instruction(ABC):
    """Base instruction class."""


class Program(Instruction):
    """Program instruction class."""

    def __init__(self, instruction: Instruction):
        self.instructions = instruction


class ConstantInstruction(Instruction):
    """Constant instruction class."""

    def __init__(self, value: str, constant_type):
        self.value = value
        self.constant_type = constant_type


class IdentifierInstruction(Instruction):
    """Identifier instruction class."""

    def __init__(self, identifier: str):
        self.identifier = identifier


class BinaryOperation(Instruction):
    """Binary operation class."""

    def __init__(
        self,
        left: Instruction,
        right: Instruction,
        op_type: OperationType,
    ):
        self.left = left
        self.right = right
        self.op_type = op_type


class CallInstruction(Instruction):
    """Call instruction class."""

    def __init__(
        self,
        identifier: str,
        arguments: List[Instruction],
    ):
        self.identifier = identifier
        self.arguments = arguments


class UnaryOperation(Instruction):
    """Represents unary operation."""

    def __init__(
        self,
        op_type: OperationType,
        operand: Instruction,
    ):
        self.op_type = op_type
        self.operand = operand
