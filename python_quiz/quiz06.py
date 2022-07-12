
# numbers = [0, 20, 100]

# a = int(numbers[i])
# b = 0
# for i in range(3) :
#     if b < a
#     b = a

# print(b)
# numbers = [0, 20, 100, 50, -60, 50, 100] # 100
# numbers = [0, 1, 0] # 1
# numbers = [-10, -100, -30] # -10 

numbers = [0, 20, 100, 50, -60, 50, 100]

max = numbers[0] # 다른 기준 float("-inf")

for i in numbers:
    if max < i:
        max = i
print(max)
