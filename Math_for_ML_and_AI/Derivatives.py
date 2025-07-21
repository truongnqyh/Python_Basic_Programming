import sympy as sp
# Declare variable
x = sp.Symbol('x')
f = x**2
derivative = sp.diff(f, x)
print("Derivative x**2 = ", derivative)
