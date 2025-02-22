from pycalc.lexing.lexer import Lexer
from pycalc.lexing.types import TokenType


def test_lexer_basic_tokenization():
    lexer = Lexer("2 + 2 * 10")

    tokens = lexer.tokenize()

    assert len(tokens) == 5

    assert tokens[0].type == TokenType.INT
    assert tokens[0].value == "2"
    assert tokens[1].type == TokenType.PLUS
    assert tokens[2].type == TokenType.INT
    assert tokens[2].value == "2"
    assert tokens[3].type == TokenType.MUL
    assert tokens[4].type == TokenType.INT
    assert tokens[4].value == "10"


def test_more_complex_tokenization():
    lexer = Lexer("(2 + 32) / 10-4.23*1 +a+b")

    tokens = lexer.tokenize()

    # Check the total number of tokens
    assert len(tokens) == 15

    # Check each token's type and value
    assert tokens[0].type == TokenType.LPAREN
    assert tokens[1].type == TokenType.INT
    assert tokens[1].value == "2"
    assert tokens[2].type == TokenType.PLUS
    assert tokens[3].type == TokenType.INT
    assert tokens[3].value == "32"
    assert tokens[4].type == TokenType.RPAREN
    assert tokens[5].type == TokenType.DIV
    assert tokens[6].type == TokenType.INT
    assert tokens[6].value == "10"
    assert tokens[7].type == TokenType.MINUS
    assert tokens[8].type == TokenType.FLOAT
    assert tokens[8].value == "4.23"
    assert tokens[9].type == TokenType.MUL
    assert tokens[10].type == TokenType.INT
    assert tokens[10].value == "1"
    assert tokens[11].type == TokenType.PLUS
    assert tokens[12].type == TokenType.IDENT
    assert tokens[12].value == "a"
    assert tokens[13].type == TokenType.PLUS
    assert tokens[14].type == TokenType.IDENT
    assert tokens[14].value == "b"


def test_super_hard_lexer_case():
    lexer = Lexer("((3.14 * -42) + 7 / (2.0 - x)) * 10.5 ^ 2 + abc123 -+5")

    tokens = lexer.tokenize()

    # Check total number of tokens
    assert len(tokens) == 25

    # Check each token's type and value
    assert tokens[0].type == TokenType.LPAREN
    assert tokens[1].type == TokenType.LPAREN
    assert tokens[2].type == TokenType.FLOAT
    assert tokens[2].value == "3.14"
    assert tokens[3].type == TokenType.MUL
    assert tokens[4].type == TokenType.MINUS  # Unary minus for -42
    assert tokens[5].type == TokenType.INT
    assert tokens[5].value == "42"
    assert tokens[6].type == TokenType.RPAREN
    assert tokens[7].type == TokenType.PLUS
    assert tokens[8].type == TokenType.INT
    assert tokens[8].value == "7"
    assert tokens[9].type == TokenType.DIV
    assert tokens[10].type == TokenType.LPAREN
    assert tokens[11].type == TokenType.FLOAT
    assert tokens[11].value == "2.0"
    assert tokens[12].type == TokenType.MINUS
    assert tokens[13].type == TokenType.IDENT
    assert tokens[13].value == "x"
    assert tokens[14].type == TokenType.RPAREN
    assert tokens[15].type == TokenType.RPAREN
    assert tokens[16].type == TokenType.MUL
    assert tokens[17].type == TokenType.FLOAT
    assert tokens[17].value == "10.5"
    assert tokens[18].type == TokenType.POW  # Assuming ^ is supported
    assert tokens[19].type == TokenType.INT
    assert tokens[19].value == "2"
    assert tokens[20].type == TokenType.PLUS
    assert tokens[21].type == TokenType.IDENT
    assert tokens[21].value == "abc123"
    assert tokens[22].type == TokenType.MINUS
    assert tokens[23].type == TokenType.PLUS
    assert tokens[24].type == TokenType.INT
    assert tokens[24].value == "5"
