class Parser:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")
        self.pos = 0

    def get_next_token(self):
        while self.pos < len(self.expression):
            char = self.expression[self.pos]
            if char.isdigit():
                start = self.pos
                while self.pos < len(self.expression) and self.expression[self.pos].isdigit():
                    self.pos += 1
                return int(self.expression[start:self.pos])
            elif char in "+-*/":
                self.pos += 1
                return char
            else:
                raise ValueError(f"Unexpected character: {char}")
        return None

    def parse_expression(self):
        result = self.parse_term()
        while self.pos < len(self.expression):
            op = self.get_next_token()
            if op == "+":
                result += self.parse_term()
            elif op == "-":
                result -= self.parse_term()
            else:
                raise ValueError(f"Unexpected operator: {op}")
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.pos < len(self.expression):
            op = self.get_next_token()
            if op == "*":
                result *= self.parse_factor()
            elif op == "/":
                divisor = self.parse_factor()
                if divisor == 0:
                    raise ZeroDivisionError("Division by zero")
                result /= divisor
            else:
                break
        return result

    def parse_factor(self):
        token = self.get_next_token()
        if token is None:
            raise ValueError("Expected a value")
        elif isinstance(token, int):
            return token
        elif token == "(":
            result = self.parse_expression()
            closing = self.get_next_token()
            if closing != ")":
                raise ValueError("Expected ')'")
            return result
        else:
            raise ValueError(f"Unexpected token: {token}")

    def evaluate(self):
        return self.parse_expression()