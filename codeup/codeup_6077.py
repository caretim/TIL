# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
n =int(input())


sum = 0


for i in range(n+1):
    if n > 100:
        print('100이하의 수를 입력해주세요')
        break
    elif i%2==0:
         sum += i

print (sum)

