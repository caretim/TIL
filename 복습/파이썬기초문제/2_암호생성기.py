from collections import deque
# import sys

# sys.stdin = open("_암호생성기.txt")
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    number=list(map(int,input().split()))

    number = deque(number)

    while True:
        for i in range(1,6):
            num = number.popleft()
            num -=  i
            if num <= 0:
                num = 0 
                number.append(num)
                # print(t,end=' ')
                # print(*number)
                break
            else:
                number.append(num)
        if number[-1] == 0:
            break 
    result= []
    for r in number:
        result.append(str(r))
    re =' '.join(result)
    print(f'#{test_case} {re}')
