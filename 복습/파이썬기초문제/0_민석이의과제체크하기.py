import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    p,s =map(int,input().split())
    sp = list(map(int,input().split()))
    people=[]
    people=set(people)
    sp=set(sp)
    
    for pn in range(1,p+1):
        people.add(pn)

    nw = people - sp
    result=[]
    for r in nw:
        result.append(str(r)) 
    re= ' '.join(result)
    print(f'#{test_case} {re}')