import sys
sys.stdin = open("input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):



    num =[]
    num=list(map(int,input().split()))
    scnt=0
    for i in range(1,16):
        if i % 2 == 0:
            scnt+= num[i-1]
        else :
            scnt+= num[i-1]*2

    if scnt%10 == 0:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {10-(scnt%10)}')