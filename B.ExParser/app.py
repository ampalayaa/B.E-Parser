from pars3r import parse_expression
from simplifier import simplify_expression


def main():
    expression = input("Enter a Boolean expression: ")
    simplified_expression = parse_expression(expression)
    print("Original Expression:", expression)
    print("Simplified Expression:", simplified_expression)

if __name__ == "__main__":
    main()