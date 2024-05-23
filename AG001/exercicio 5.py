from sympy import Symbol,exp, solve, sin

c = 1938 % 10
x = Symbol('x')
w = Symbol('w')
a = Symbol('a')

def eq1(x):
    return exp(x-3)+exp(x-1)+exp(x)-(c+1)

def eq2(w):
    return (w ** 4) - (4 * w ** 3) + (3 * w) - c

def eq3(a):
    return (4*sin((c+1)*a)+2)


y = eq1(x)
result1 = solve(y)

z = eq2(w)
result2 = solve(z)

b = eq3(a)
result3 = solve(b)

print("Resultado da equação 1: ", result1)
print("Resultado da equação 2: ", result2)
print("Resultado da equação 3: ", result3)