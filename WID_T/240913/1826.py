import sys,heapq
input = sys.stdin.readline

n = int(input())

heap = []

for __ in range(n):
    a,b = map(int,input().split())
    heap.append((a,b))



end,now_oil = map(int,input().split())

stations = []
heap.append((end,0))

heap.sort()
result=0
#도달못하는 경우 
for next,nextOil in heap:
    if now_oil<end and stations:
        while now_oil<next and stations:
            plusoil = heapq.heappop(stations)
            now_oil+=(-plusoil)
            result+=1
        if now_oil<next:
            result=-1
            break
    heapq.heappush(stations,-nextOil)



print(result)