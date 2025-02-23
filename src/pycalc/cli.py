from argparse import ArgumentParser

from pycalc.calculator import calc


def build_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="pycalc", description="A simple calculator", epilog="Help"
    )

    parser.add_argument("--expression", type=str, required=False)

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

    # If there's no arguments, we run an interactive shell.
    if args.expression:
        try:
            res = calc(args.expression)
        except Exception as e:
            print(e)
            return

        print(res)

    repl()
