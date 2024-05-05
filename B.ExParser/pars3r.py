class TokenType:
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    VARIABLE = "VARIABLE"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    EOF = "EOF"

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

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

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == TokenType.VARIABLE:
            self.eat(TokenType.VARIABLE)
            return token.value
        elif token.type == TokenType.NOT:
            self.eat(TokenType.NOT)
            return "NOT " + self.factor()
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            result = self.expr()
            self.eat(TokenType.RPAREN)
            return result

    def term(self):
        result = self.factor()
        while self.current_token.type in (TokenType.AND,):
            if self.current_token.type == TokenType.AND:
                self.eat(TokenType.AND)
                result += " AND " + self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token.type in (TokenType.OR,):
            if self.current_token.type == TokenType.OR:
                self.eat(TokenType.OR)
                result += " OR " + self.term()
        return result

def parse_expression(expression):
    try:
        lexer = Lexer(expression)
        parser = Parser(lexer)
        return parser.expr()
    except Exception as e:
        raise Exception(f"Error parsing expression: {e}")