# import sys

# sys.stdin = open("_파리퇴치.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    m,n = map(int,input().split())


    matrix= [list(map(int,input().split())) for __ in range(m)]

    pari= []
    for y in range(0,m-n+1):
        for x in range(0,m-n+1):
            cnt =0
            for j in range (n):
                for i in range(n):
                    cnt+= matrix[y+j][x+i]
            pari.append(cnt)

    print(f'#{test_case} {max(pari)}')
            



                          
