import sys
import heapq
input= sys.stdin.readline

n,k =map(int,input().split())

#각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
#보석은 무게 Mi와 가격 Vi
jewel = [list(map(int,input().split())) for __ in range(n)]
#가방 중복판매 방지 -> 가방에 담은 보석의 가치 0으로 변경 
bags = []

for __  in range(k):
    bags.append(int(input().rstrip()))

jewel.sort()
bags.sort()

values= [] #가치가 제일 큰 보석만 뽑으면 됨 

now = 0
flag= 0
result = 0

for bw in bags:
    for i in range(now,len(jewel)):# 틀리는 부분이 여기일거같은데
        if flag:
            break
        if jewel[i][0]<=bw:
            heapq.heappush(values,-jewel[i][1])
            if i == len(jewel)-1:
                flag=1
        else:
            break
    now = i #가방 범위 이내의 인덱스 모두 방문해야함 
    if values: # 0개일떄 인덱스 오류 발생
        result-=heapq.heappop(values)

print(result)





    

