import sys,heapq

input =sys.stdin.readline

n= int(input())

times = []
for i in range(n):
    start,end = map(int,input().split())
    heapq.heappush(times,(start,1))
    heapq.heappush(times,(end,-1))

result = 0
cnt = 0
while times:
    time,val = heapq.heappop(times)
    cnt+=val
    result = max(result,cnt)

print(result)


