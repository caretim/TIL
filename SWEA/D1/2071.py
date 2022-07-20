


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sq = 10
    a = map(int,input().split())
    d = sum(a)/sq
    print(f'#{test_case} {round(d)}') 
    # for i in range(sq):
    #     n = input()
    #     count += int(n)
    # print(f'#{test_case} {count/sq}') 
    