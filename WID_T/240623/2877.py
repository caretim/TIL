
# 4 , 7 
# 2로 나누었을때 나머지를 기준으로 숫자 배치
# 1 - 3 4  2 - 5 6 

# 3 - 7 8 4 -  9 10

n= int(input())


n= bin(n+1)

result = ''
for i in str(n)[3:]:
    if i == '0': result+='4' 
    elif i == '1': result+='7'

print(result)

# result = ''


# while n:
#     if n % 2 ==0:
#         result+='0'
#     elif n%2 == 1:
#         result+='1'
#     n= n//2

# # result+=str(n)


# # 1:4 2:7  3:44 4:47 5:74 6:77  7:444 8:447 9:474 10:477 11:744 12:747 13:774 14: 777  15 :4444 16 :4447
# # 17: 4474 18:4477
# print(result[1:])