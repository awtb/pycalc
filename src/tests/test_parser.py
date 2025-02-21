from pycalc.lexing.lexer import Lexer
from pycalc.parsing.parser import Parser
from pycalc.parsing.types import BinaryOperation, OperationType, ConstantInstruction


def test_basic_parser():
    lexer = Lexer("2 + 2 * 3")
    tokens = lexer.tokenize()

    parser = Parser(tokens)

    instruction = parser.parse()

    assert isinstance(instruction, BinaryOperation)
    assert isinstance(instruction.left, ConstantInstruction)
    assert isinstance(instruction.right, BinaryOperation)

    assert instruction.right.op_type == OperationType.MULTIPLICATION

    assert isinstance(instruction.right.left, ConstantInstruction)
    assert isinstance(instruction.right.right, ConstantInstruction)

    assert instruction.right.left.value == "2"
    assert instruction.right.right.value == "3"


def test_complex_parser():
    # Initialize lexer with the expression
    lexer = Lexer("2 * 3 - 4 * 5 + 6 * 7")
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    instruction = parser.parse()

    # Top-level operation: addition
    assert isinstance(instruction, BinaryOperation)
    assert instruction.op_type == OperationType.ADDITION

    # Left child of addition: subtraction
    assert isinstance(instruction.left, BinaryOperation)
    assert instruction.left.op_type == OperationType.SUBTRACTION

    # Left child of subtraction: multiplication of 2 and 3
    assert isinstance(instruction.left.left, BinaryOperation)
    assert instruction.left.left.op_type == OperationType.MULTIPLICATION
    assert isinstance(instruction.left.left.left, ConstantInstruction)
    assert instruction.left.left.left.value == "2"
    assert isinstance(instruction.left.left.right, ConstantInstruction)
    assert instruction.left.left.right.value == "3"

    # Right child of subtraction: multiplication of 4 and 5
    assert isinstance(instruction.left.right, BinaryOperation)
    assert instruction.left.right.op_type == OperationType.MULTIPLICATION
    assert isinstance(instruction.left.right.left, ConstantInstruction)
    assert instruction.left.right.left.value == "4"
    assert isinstance(instruction.left.right.right, ConstantInstruction)
    assert instruction.left.right.right.value == "5"

    # Right child of addition: multiplication of 6 and 7
    assert isinstance(instruction.right, BinaryOperation)
    assert instruction.right.op_type == OperationType.MULTIPLICATION
    assert isinstance(instruction.right.left, ConstantInstruction)
    assert instruction.right.left.value == "6"
    assert isinstance(instruction.right.right, ConstantInstruction)
    assert instruction.right.right.value == "7"