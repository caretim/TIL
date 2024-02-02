import heapq
 
n = int(input())
 
heap = []
 
for i in range(n):
    candidate = int(input())
    
    if i == 0:
        dasom = candidate #
        continue
 
    heapq.heappush(heap, -candidate)
 
cnt = 0
 
while heap:
    candidate = - heapq.heappop(heap) 
 
    if candidate < dasom: 
        break
 
    else :
        dasom += 1
        candidate -= 1
        cnt += 1
 
        heapq.heappush(heap, -candidate)
 
print(cnt)