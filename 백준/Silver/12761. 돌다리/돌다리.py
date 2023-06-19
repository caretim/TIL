from collections import deque
import heapq
import sys
a,b,n,m=map(int,input().split())

INF =sys.maxsize

# +1칸, -1칸을 이동할 수 있고, 
# A나 B만큼 좌우로 점프할 수 있으며, 순간적으로 힘을 모아 현 위치의 
# A 배나 B배의 위치로 이동을 할 수 있다. 

arr=[INF]*100001

def bfs(a,b,n,m):
    q=[]
    arr[n]=0
    heapq.heappush(q,(0,n))
    # q.append((0,n))
    while q:
        cnt,now = heapq.heappop(q)
        for i in (now+1,now-1,now*a,now*b,now-a,now+a,now+b,now-b):
            if 0<=i<100001 and arr[i]==INF:
                arr[i]=cnt+1
                heapq.heappush(q,(cnt+1,i))

    print(arr[m])


bfs(a,b,n,m)