from sympy.logic.boolalg import And, Or, Not
from sympy.abc import symbols
from sympy.logic.boolalg import to_dnf
from pars3r import *

def simplify_expression(expression):
    vars = set() # -> Define symbols for variables
    for char in expression:
        if char.isalnum():
            vars.add(char)
    vars = symbols(vars)
    sym_vars = {str(var): var for var in vars} # -> Create dictionary mapping variable names to their corresponding SymPy symbols
    sympy_expr = eval(expression, {**sym_vars, 'And': And, 'Or': Or, 'Not': Not}) # -> Parse the expression into a SymPy expression
    dnf_expr = to_dnf(sympy_expr) # -> onvert to Disjunctive Normal Form (DNF)
    return str(dnf_expr) # _> Convert back to string representation