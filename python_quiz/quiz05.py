
#처음에 생각했던것, 인덱스 값을 정수화시켜
#인덱스 갯수로 range를 구하는 방법
# num = [3, 10 , 20]

# a = 0
# x = 0
# for i in range(num):
#     a = a +1
#     x = num[int(a)] 
#     x += x

# print(int(x)/a)


#range를 3으로 줘서 문제 풀이
num = [3, 10 , 20]

a = 0
x = 0
y = 0
for i in range(3): # 인덱스의 개체 숫자를 세는법 알아보기
    a = a +1
    x = num[int(i)] 
    y = y+ x

print(int(y)/a)



#해설 답안



# numbers= [ 3, 10 , 20]
# # 값 초기화

# r = 0
# c = 0


# #.반복

# for number in numbers:

#     r = r + numbers

#     c = c + 1

# print(r/c)
