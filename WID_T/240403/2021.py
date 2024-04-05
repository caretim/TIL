import sys

import heapq

INF = sys.maxsize

n,m= map(int,input().split())

station = [[] for __ in range(n+1)]
train = []


station_visited = [INF]*(n+1)
train_visited = [INF]*(m+1)



for i in range(m):
    TL = list(map(int,input().split()))
    train.append(TL[:-1])
    for t in range(len(TL)-1):
        station[TL[t]].append(i)

start,end = map(int,input().split())

start= set(station[start])
end = set(station[end])


def dijkstra(start,end):
    set_ = set()
    for s in start:
        train_visited[s] =0
        set_.add((0,s))
    while set_:
        cnt,now =set_.pop()
        if now in end:
            return cnt

        if train_visited[now] < cnt:
            continue

        for line in train[now]:
            if train_visited[line]<cnt:
                continue

            for t in station[line]:
                if train_visited[t]>cnt+1:
                    train_visited[t]=cnt+1
                    set_.add((cnt+1,t))
        

print(dijkstra(start,end))

