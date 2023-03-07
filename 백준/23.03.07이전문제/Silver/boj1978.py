# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

n = int(input())

count = 0

nlist = map(int, input().split())

count = 0
for i in nlist:
    no = 0
    if i == 1:
        no += 1
        pass
    else:
        for j in range(2, i):
            if i % j == 0:
                no += 1
    if no == 0:
        count += 1


print(count)
