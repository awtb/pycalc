from argparse import ArgumentParser

from pycalc.calculator import calc
from pycalc.lexing.lexer import Lexer
from pycalc.parsing.parser import Parser


def build_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="pycalc", description="A simple calculator", epilog="Help"
    )

    parser.add_argument("--expression", type=str, required=False)
    parser.add_argument("--show-tokens", action="store_true")
    parser.add_argument("--show-ast", action="store_true")

    return parser


def repl():
    """
    Runs interactive calculator
    :return:
    """
    print("PyCalc interactive shell.")
    print("Use .exit for exit.")
    while True:
        expr = input(">> ")

        if expr == ".exit":
            break

        try:
            result = calc(expr)
        except Exception as e:
            print(e)
            continue

        print(result)


def main():
    parser = build_argument_parser()

    args = parser.parse_args()

    if args.show_tokens:
        lexer = Lexer(args.expression)
        tokens = lexer.tokenize()

        print("Tokens:", tokens)

    if args.show_ast:
        lexer = Lexer(args.expression)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        print("AST:", ast)

    # If there's no arguments, we run an interactive shell.
    if args.expression:
        try:
            res = calc(args.expression)
        except Exception as e:
            print(e)
            return

        print(res)

    repl()
