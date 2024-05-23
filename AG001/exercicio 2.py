from sympy import Symbol, Integral, sqrt, Derivative

C = 1939 % 10

x = Symbol('x')

def minhaFuncao(x):
    return 5 * C + 7 * (x ** 4) + x ** (1/3) - 3 * C * x ** 3

y = Integral(minhaFuncao(x), x).doit()
print('deslocamento =', y)

z = Derivative(minhaFuncao(x), x).doit()
print('aceleracao =', z)

d = Integral(minhaFuncao(x), (x, 1, 7)).doit()
print('1 a 7 s =', d)
