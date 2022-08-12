# num = [ 0, 20, 100, 50, -60, 50, 100]
# max = num[0]

# for i in num:
#     if max <= i:
#         max =i


# num.remove(max)

# max = num[0]

# for i in num:
#     if max <= i:
#         max =i

# print(max)

num = [ 120 , 20, 40,60,30,95]
max = 0
second = num[0]

for n in num:
    if max <= n:
        second =max
        max = n
    elif second< n < max:
        second = n     
print(second)
