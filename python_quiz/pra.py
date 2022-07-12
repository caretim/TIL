

numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30


min = numbers[0]
lage = 0
second = 0

for i in numbers:
    if min >= i:
        second = min
        min = i


print(second)


# # num = [3, 10 , 20]

# # # a = 0
# # x = 0
# # y = 0
# # for i in range(3): # 인덱스의 개체 숫자를 세는법 알아보기
# #     a = a +1
# #     x = num[int(i)] 
# #     y = y+ x

# # print(int(y)/a)





# numbers= [ 3, 10 , 20]
# # 값 초기화

# r = 0
# c = 0


# #.반복

# for number in numbers:

#     r = r + numbers

#     c = c + 1

# print(r/c)
