# for i in range(len(numbers)):
#     # if i == len(numbers) - 1:
#     #     result.append(-1)
#     num = -1
#     for k in range(i, len(numbers)):
#         if numbers[i] < numbers[k]:
#             num = numbers[k]
#             break
#     result.append(num)

# print(result)
numbers = [2, 3, 3, 5]

result = []
check_num = numbers[0]

count = 0
for i in range(len(numbers)):
    count += 1
    if numbers[i] > check_num:
        for __ in range(count):
            result.append(numbers[i])
            # print(numbers[i])
        count = 0
    check_num = numbers[i]


for __ in range(count):
    result.append(-1)

print(result)
