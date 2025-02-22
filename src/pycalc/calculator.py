from pycalc.evalulation.evaluator import Evaluator
from pycalc.lexing.lexer import Lexer
from pycalc.parsing.parser import Parser


def calc(expression: str) -> float:
    """
    Calculate an expression
    :param expression: Just expression
    :return:
    """
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    tree = parser.parse()
    evaluator = Evaluator(tree[0])

    return evaluator.evaluate()
