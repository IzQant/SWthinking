#Sigmoid
import math
x = int(input("x >"))
exp = 0
for i in range(100):
    exp += x**i / math.factorial(i)
print(exp)

sigmoid = 1 / (1 + 1/exp)
print(sigmoid)
