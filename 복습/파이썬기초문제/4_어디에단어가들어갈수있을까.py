import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n,m= map(int,input().split())

    matrix= [list(map(int,input().split())) for __ in range(n)]

    canword=0

    for words in matrix:
        spcnt=0
        for char in words:
            if char == 1:
                spcnt += 1
            elif char == 0:
                if spcnt == m:
                    canword += 1

                    spcnt =0
                else:
                    spcnt =0
        if spcnt == m:
            canword += 1
            spcnt=0

        else:
            spcnt=0

    for x in range(n):
        lpcnt=0
        for y in range(n):
            if matrix[y][x] == 1:
                lpcnt += 1

            elif matrix[y][x] == 0:
                if lpcnt == m:
                    canword += 1
                    lpcnt =0


                else:
                    lpcnt =0
        if lpcnt == m:
            canword += 1
            lpcnt=0
        else:
            lpcnt=0

    # print(canword)
    print(f'#{test_case} {canword}')
            


