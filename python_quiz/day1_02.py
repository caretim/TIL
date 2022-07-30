from posixpath import split



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n= int(input())

    pp =[]
    pp = list(map(int,input().split()))

    avpp= sum(pp)/n

    cnt=0

    for i in pp:
        if i <=avpp:
            cnt+=1

    print(f'#{test_case} {cnt}')