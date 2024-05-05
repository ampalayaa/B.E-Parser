# Token types
class TokenType:
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    VARIABLE = "VARIABLE"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    EOF = "EOF"

# Token class
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

# Lexer class
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def variable(self):
        result = ""
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '&':
                self.advance()
                return Token(TokenType.AND)

            if self.current_char == '|':
                self.advance()
                return Token(TokenType.OR)

            if self.current_char == '!':
                self.advance()
                return Token(TokenType.NOT)

            if self.current_char == '~':
                self.advance()
                return Token(TokenType.NOT)

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN)

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN)

            if self.current_char.isalnum():
                return Token(TokenType.VARIABLE, self.variable())

            self.error()

        return Token(TokenType.EOF)