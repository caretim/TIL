# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.



n = int(input())
a = 0
print(a)
while a <= n -1:
        a += 1
        if a == 101:
                break
        print (a)
