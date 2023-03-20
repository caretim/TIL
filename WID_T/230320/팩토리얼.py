def factorial(n):
    result = 0
    if n > 0:
        result = n * factorial(n - 1)
    return result


n = int(input())
print(factorial(n))
