from src.pycalc.lexing.lexer import Lexer


def main():
    lexer = Lexer(
        "2.4 + 123 * 3"
    )

    tokens = lexer.tokenize()


    for token in tokens:
        print(token, end=' ')

if __name__ == "__main__":
    main()