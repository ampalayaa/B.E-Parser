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
        """
        Token representation.

        :param type: Token type
        :param value: Token value (optional)
        """
        self.type = type
        self.value = value

class LexerError(Exception):
    """Lexer error exception."""

class Lexer:
    def __init__(self):
        """
        Lexer initialization.
        """
        self.text = None
        self.pos = 0
        self.current_char = None
        self.tokens = []

    def input_text(self, text: str):
        """
        Set input text.

        :param text: Input text
        """
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        """
        Raise a lexer error.
        """
        raise LexerError("Invalid character")

    def advance(self):
        """
        Advance to the next character.
        """
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """
        Skip whitespace characters.
        """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def handle_word(self):
        """
        Handle word tokens (e.g., AND, OR, VAR).
        """
        value = ""
        while self.current_char is not None and self.current_char.isalnum():
            value += self.current_char
            self.advance()
        if value.lower() in ["and", "or"]:
            self.tokens.append(Token(TokenType[value.upper()], value))
        else:
            self.tokens.append(Token(TokenType.VAR, value))

    def handle_number(self):
        """
        Handle number tokens.
        """
        value = ""
        while self.current_char is not None and self.current_char.isdigit():
            value += self.current_char
            self.advance()
        self.tokens.append(Token(TokenType.NUMBER, int(value)))

    def handle_single_char_token(self):
        """
        Handle single-character tokens (e.g., +, *, (, )).
        """
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
        """
        Get the next token.

        :return: List of tokens
        """
        self.tokens = []  # Clear previous tokens
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