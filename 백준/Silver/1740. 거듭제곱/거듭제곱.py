n = int(input())

num = list(bin(n)[2:])[::-1]

t, result = 1, 0
for i in num:
    result += int(i)*t
    t *= 3
print(result)