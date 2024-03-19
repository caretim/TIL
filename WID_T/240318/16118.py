import sys
import heapq

input =sys.stdin.readline

INF =sys.maxsize

n,m =map(int,input().split())


graph= [[] for __ in range(n)]

f_v=[INF]*(n)

w_v=[[INF]*(n) for __ in range(2)]



for __ in range(m):
    u,v,w= map(int,input().split())
    u-=1;v-=1
    graph[u].append((w,v))
    graph[v].append((w,u))


def dijkstra(start):
    heap=[]
    heapq.heappush(heap,(0,start,0,0)) # 여우
    heapq.heappush(heap,(0,start,1,0)) # 늑대
    f_v[0]=0
    w_v[1][0]=0

    while heap:
        w,now,fw,cnt= heapq.heappop(heap)
        if fw ==0 and f_v[now]<w:
            continue
        elif fw ==1:
            if cnt and w_v[0][now]<w:
                continue
            elif not cnt and w_v[1][now]<w:
                continue
        
        for nextCost,nextNode in graph[now]:
            if fw==0:
                cost = w+nextCost
                if f_v[nextNode]>cost:
                    f_v[nextNode]=cost
                    heapq.heappush(heap,(cost,nextNode,fw,cnt))
            elif fw ==1:
                if cnt:
                    cost = w+(nextCost*2)
                    if w_v[1][nextNode]>cost:
                        w_v[1][nextNode]=cost
                        heapq.heappush(heap,(cost,nextNode,fw,False))
                else:
                    cost = w+(nextCost/2)
                    if w_v[0][nextNode]>cost:
                        w_v[0][nextNode]=cost
                        heapq.heappush(heap,(cost,nextNode,fw,True))

dijkstra(0)

result=0
for i in range(n):
    if f_v[i]< w_v[0][i] and f_v[i]<w_v[1][i]:
        result+=1

# print(f_v,w_v)

print(result)
                    
                
