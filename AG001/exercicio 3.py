from sympy import Symbol, Integral, sqrt

C = 1938 % 10

def minhaFuncao(x):
    return 5*x**3 + sqrt(((x/3)**3),5) + (3/4)*x - 3*C

if __name__ == '__main__':
    x = Symbol('x')
    result = Integral(minhaFuncao(x), (x, 3, 8)).doit()
    print(result)