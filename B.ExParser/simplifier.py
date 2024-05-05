from sympy.logic.boolalg import And, Or, Not
from sympy.abc import symbols
from sympy.logic.boolalg import to_dnf
from pars3r import parse_expression  # Corrected import statement

def simplify_expression(expression):
    # Define symbols for variables
    vars = symbols(set(expression) - set("&|!() "))

    # Create a dictionary mapping variable names to their corresponding SymPy symbols
    sym_vars = {str(var): var for var in vars}

    # Parse the expression into a SymPy expression
    sympy_expr = eval(expression, {**sym_vars, 'And': And, 'Or': Or, 'Not': Not})

    # Convert to Disjunctive Normal Form (DNF)
    dnf_expr = to_dnf(sympy_expr)

    # Convert back to string representation
    return str(dnf_expr)
