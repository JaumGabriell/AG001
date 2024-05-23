from sympy import Eq, symbols, solve

c = 1939 % 10

I1, I2, I3 = symbols('I1 I2 I3')

V1 = 7 + (5 * c)
V2 = 4 + (2 * c)
V3 = 3 + (4 * c)

R1, R2, R3 = 15000, 5000, 10000

eq1 = Eq(I3, I2 + I1)
eq2 = Eq(0, -V1 + R1 * I1 + V2 - R2 * I2)
eq3 = Eq(0, -R2 * I2 + V2 - R3 * I3 - V3)

results = solve((eq1,eq2,eq3),(I1,I2,I3))

print('I1 = ', results[I1])
print('I2 = ', results[I2])
print('I3 = ', results[I3])