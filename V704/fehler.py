import numpy as np
import sympy

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols

    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\Delta{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

R = sympy.var(r'R_\text{max}')

f = 1.92*sympy.sqrt(R**2 + 0.22*R)
print(f)
print(error(f))
print()
