import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n= int(input())

station = list(map(int,input().split()))


graph = [[[]for __ in range(station[i])] for i in range(n)]

def dijkstra(tr,s1,s2,e1,e2):
    visit =[[INF]* station[i] for i in range(n)]
    visit[s1][s2]=0
    q=[]
    heapq.heappush(q,(0,s1,s2))
    while q:
        move,u1,u2 = heapq.heappop(q)
        if visit[u1][u2]<move:
            continue
        # if (u1,u2) == (e1,e2):
        #     print(move)
        #     return
        for next_u1,next_u2 in graph[u1][u2]:
            if u1==next_u1 and  visit[next_u1][next_u2]>move+1:
                visit[next_u1][next_u2] = move+1
                heapq.heappush(q,(move+1,next_u1,next_u2))  
            elif u1!=next_u1 and visit[next_u1][next_u2]>move+tr:
                visit[next_u1][next_u2] = move+tr
                heapq.heappush(q,(move+tr,next_u1,next_u2))
    return print(visit[e1][e2])
    



for i in range(n):
    for j in range(station[i]):
        if j -1 >= 0:
            graph[i][j].append((i,j-1))
        if j+1 < station[i]:
            graph[i][j].append((i,j+1))

m= int(input())

for __ in range(m):
    p1,p2,q1,q2= map(int,input().split())
    p1-=1;p2-=1; q1-=1; q2-=1 # 오..세미콜론으로 동일한 줄에 변수 여러개 설정,
    graph[p1][p2].append((q1,q2))
    graph[q1][q2].append((p1,p2))

k= int(input())


for __ in range(k):
    tr,s1,s2,e1,e2 =map(int,input().split())
    s1-=1;s2-=1; e1-=1; e2-=1
    dijkstra(tr,s1,s2,e1,e2)

