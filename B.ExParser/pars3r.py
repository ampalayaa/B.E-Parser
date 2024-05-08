from tokenizer import TokenType, Lexer

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