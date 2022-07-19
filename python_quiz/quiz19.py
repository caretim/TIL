# > 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# **양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지**

 # if 문으로 10, 100 100마다 +1씩 되게만들기
 # 숫자를 리스트로 만들어서 슬라이스로 for문 돌리기 

# Input
# 123


# Output
#3

cnt= 1
num= int(input())
j = 10
while j > 0:
    if num/j > 0:
        j = 10**cnt
        cnt+=1
        if j >=num:
            break
print (cnt-1)

num = 123456

while num != 0: #종료조건때까지 ,while이 참이 되는순간까지
    num //= 10 # num = num // 10 
    cnt = 1  #num 나누기 10의 몫을 계속해서 10으로 나눠준다 0이되는순간까지
             # 한번 반복할때마다 카운트를 하나씩 추가해준다.


#지수로도 구할 수 있다.




# num = (input().split())


# print(num)
# cnt = 0
# for i in num[0:]:
#     cnt+= 1



# nums =int(input())
# cnt = 0
# if nums/10000 >0:
#     cnt= 4
# elif nums/1000 >0:
#      cnt= 3
# elif nums/100 >0:
#       cnt = 2
# elif nums/10>0:
#         cnt = 1
# print(cnt)


# # nums =int(input())
# cnt = 0
# if nums/10000 >0:
#     cnt= 4
# elif nums/1000 >0:
#      cnt= 3
# elif nums/100 >0:
#       cnt = 2
# elif nums/10>0:
#         cnt = 1
# print(cnt)