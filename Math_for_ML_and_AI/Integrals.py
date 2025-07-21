import sympy as sp

x = sp.Symbol('x')
f = sp.exp(-x)

indefinite_integral = sp.integrate(f, x)
print("Indefinite Integral: " ,indefinite_integral)
definite_integral = sp.integrate(f, (x, 0, sp.oo))
print("Definite Integral: ",definite_integral)