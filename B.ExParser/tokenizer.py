# tokenizer.py
from enum import Enum

class TokenType(Enum):
    EOF = 0
    VAR = 1
    PLUS = 2
    MUL = 3
    LPAREN = 4
    RPAREN = 5
    AND = 6
    OR = 7
    NUMBER = 8

class Token:
    def __init__(self, type: TokenType, value: str = None):
        self.type = type
        self.value = value

class LexerError(Exception):
    """Lexer error exception."""

class Lexer:
    def __init__(self):
        self.text = None
        self.pos = 0
        self.current_char = None
        self.tokens = []

    def input_text(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise LexerError("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def handle_word(self):
        value = ""
        while self.current_char is not None and self.current_char.isalnum():
            value += self.current_char
            self.advance()
        if value.lower() in ["and", "or"]:
            self.tokens.append(Token(TokenType[value.upper()], value))
        else:
            self.tokens.append(Token(TokenType.VAR, value))

    def handle_number(self):
        value = ""
        while self.current_char is not None and self.current_char.isdigit():
            value += self.current_char
            self.advance()
        self.tokens.append(Token(TokenType.NUMBER, int(value)))

    def handle_single_char_token(self):
        if self.current_char == '+':
            self.tokens.append(Token(TokenType.PLUS, '+'))
        elif self.current_char == '*':
            self.tokens.append(Token(TokenType.MUL, '*'))
        elif self.current_char == '(':
            self.tokens.append(Token(TokenType.LPAREN, '('))
        elif self.current_char == ')':
            self.tokens.append(Token(TokenType.RPAREN, ')'))
        else:
            self.error()
        self.advance()

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                self.handle_word()
                continue

            if self.current_char.isdigit():
                self.handle_number()
                continue

            if self.current_char in "+*()":
                self.handle_single_char_token()
                continue

            self.error()

        self.tokens.append(Token(TokenType.EOF))
        return self.tokens

    def get_all_tokens(self):
        # Make a copy of self.tokens to avoid modifying it
        tokens_copy = self.tokens[:]
        return tokens_copy

    def format_tokens(self, tokens: list[Token]) -> str:
        token_strings = [f'"{token.type.name}"' if token.type != TokenType.VAR else f'"{token.value}"' for token in tokens]
        return " | ".join(token_strings) + " | EOF"