from math import factorial, pow
n = int(input())
print(factorial(n) % int(pow(10, len(str(n)))))