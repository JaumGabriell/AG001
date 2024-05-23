from sympy import Symbol, Limit, S

C = 1939 % 10

def minhaFuncao(x):
    return (1+C)*(2*x**2-7)/(7*x**5-2)


if __name__ == '__main__':
    x = Symbol('x')

    result = Limit(minhaFuncao(x), x,1 ).doit()
    print(f'\nX -> 0: {result}')

    result = Limit(minhaFuncao(x), x, S.Infinity).doit()
    print(f'\nX -> oo: {result}')

    result = Limit(minhaFuncao(x), x, -S.Infinity).doit()
    print(f'\nX -> -oo: {result}')