import sys

import heapq

INF = sys.maxsize

n,m= map(int,input().split())

station = [[] for __ in range(n+1)]
train = []


station_visited = [INF]*(n+1)
train_visited = [0]*(m+1)



for i in range(m):
    TL = list(map(int,input().split()))
    train.append(TL[:-1])
    for t in range(len(TL)-1):
        station[TL[t]].append(i)

start,end = map(int,input().split())

def dijkstra(start,end):
    heap= []
    station_visited[start]=0
    heapq.heappush(heap,(0,start))

    while heap:
        cnt,now= heapq.heappop(heap)
        if station_visited[now]<cnt:
            continue
        for next_line in station[now]:
            if train_visited[next_line]==1:
                continue
            train_visited[next_line] =1
            for s in train[next_line]:
                if s == end:
                    return cnt
                if station_visited[s]>cnt+1:
                    station_visited[s]=cnt+1
                    heapq.heappush(heap,(cnt+1,s))
    return -1

print(dijkstra(start,end))



# for l in station[start]:
#         train_visited[l] =0
#     heapq.heappush(heap,(0,start))

#     while heap:
#         cnt,now =heapq.heappop(heap)
#         if station_visited[now] < cnt: # 역 방문 
#             continue

#         for line in station[now]: # 해당역의 호선 순회

#             if train_visited[line]<cnt+1: # 만약 해당 호선의 방문리스트보다 많은 이동횟수로 방문했다면 멈춤,
#                 continue
#             for t in train[line]: #해당 역 순회. 
#                 if now == end:
#                     return cnt
#                 if station_visited[t]>cnt+1:
#                     station_visited[t]=cnt+1
#                     heapq.heappush(heap,(cnt+1,t))
        


# print(station_visited)
