import heapq 
import sys

INF = sys.maxsize

n,m = map(int,input().split())
max_a = 100001
check =[INF] *max_a

# 순간이동시에는 0초 걸림

q=[]
heapq.heappush(q,(0,n))
while q:
    j,x = heapq.heappop(q)
    if x == m:
        print(j)
        break
    for k in (x-1,x+1):
        if 0<=k < max_a:   
            if check[k]>j+1:
                check[k]=j+1
                heapq.heappush(q,(j+1,k))
    d = 2*x
    if 0<=d < max_a:
        if check[d]>j:
            check[d]=j
            heapq.heappush(q,(j,d))




        
