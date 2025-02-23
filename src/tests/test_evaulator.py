from pycalc.evalulation.evaluator import Evaluator
from pycalc.lexing.lexer import Lexer
from pycalc.parsing.parser import Parser


def test_simple_evaluation():
    expression = "2 + 2 * 2"

    lexer = Lexer(expression)
    parser = Parser(lexer.tokenize())
    instructions = parser.parse()
    evaluator = Evaluator(instructions[0])
    result = evaluator.evaluate()

    assert result == 6


def test_complex_parentheses():
    expression = "(3 + 5) * (2 - 1) / 2 + 4"

    lexer = Lexer(expression)
    parser = Parser(lexer.tokenize())
    instructions = parser.parse()
    evaluator = Evaluator(instructions[0])
    result = evaluator.evaluate()

    # Step-by-step: (3 + 5) = 8, (2 - 1) = 1, 8 * 1 = 8, 8 / 2 = 4, 4 + 4 = 8
    assert result == 8


def test_mixed_operations():
    expression = "(12 / (3 + 1)) * (2 + 4) - (6 - 2)"

    lexer = Lexer(expression)
    parser = Parser(lexer.tokenize())
    instructions = parser.parse()
    evaluator = Evaluator(instructions[0])
    result = evaluator.evaluate()

    # Step-by-step: (3 + 1) = 4, 12 / 4 = 3, (2 + 4) = 6,
    # 3 * 6 = 18, (6 - 2) = 4, 18 - 4 = 14
    assert result == 14
