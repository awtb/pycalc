from argparse import ArgumentParser

from pycalc.calculator import calc

def build_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="pycalc", description="A simple calculator", epilog="Help"
    )

    parser.add_argument("--expression", type=str, required=False)

    return parser

def repl():
    while True:
        expr = input(">> ")




def main():
    parser = build_argument_parser()

    args = parser.parse_args()

    if args.expression:
        print("Result:", calc(expression=args.expression))
        return

    while True:
        expr = input("> ")

        print("Result:", calc(expr))