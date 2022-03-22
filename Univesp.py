from sympy import *

x = symbols('x')
f = (5 * x ** 2)+(2*x)

limete = limit(f, x, 1)
print(limete)
numero = bin(1000111100111100)
print('numero {} em octagonal {}'.format(numero, hex(numero)[2:]))