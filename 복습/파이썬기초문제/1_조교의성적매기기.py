import heapq
import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    s,c = map(int,input().split())

    scores=[]
    std=[]
    for poeple in range(1,s+1):
        c1,c2,c3= map(int,input().split())
        score =(c1*0.35)+(c2*0.45)+(c3*0.2)
        sc = round(score,3)
        std.append((poeple,sc))
        scores.append(sc)


    scores.sort(reverse=True)
    heapq.heapify(std)
 
    fn=0
    for __ in range(c):
        fn = heapq.heappop(std)

    rank=0
    for sag in scores:
        rank+=1
        if sag == fn[1]:
            break

    print(f'#{test_case}',end=' ')

    if rank/s <= 0.1:
        print('A+')
    elif rank/s <=0.2:
        print('A0')
    elif rank/s <=0.3:
        print('A-')
    elif rank/s <=0.4:
        print('B+')
    elif rank/s <=0.5:
        print('B0')
    elif rank/s <=0.6:
        print('B-')
    elif rank/s <=0.7:
        print('C+')
    elif rank/s <=0.8:
        print('C0')
    elif rank/s <=0.9:
        print('C-')
    else:
        print('D0')

