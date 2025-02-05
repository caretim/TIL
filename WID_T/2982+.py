import sys,heapq


n,m= map(int,input().split())


INF=sys.stdin.readline
#A는 상근이가 배달을 시작하는 교차로, 
# B는 상근이가 배달을 마치는 교차로이다. 
# K는 고둘라가 출발한 시간과 상근이가 출발한 시간의 차이,
#  G는 고둘라가 방문하는 교차로의 개수
a,b,k,g = map(int,input().split())

# G개의 정수가 주어진다.이 정수는 고둘라가 방문하는 교차로이다. 
go_load= list(map(int,input().split()))


way = [[] for __ in range(n+1)]
check_way = [[-1 for __ in range(n+1)]for __ in range(n+1)]

print(check_way)
for i in range(m):
    u,v,w = map(int,input().split())
    way[u].append((v,w,i))
    way[v].append((u,w,i))
    check_way[u][v]=(w,i)
    check_way[v][u]=(w,i)


go_visited = []*g
visited= [INF]*n
print(check_way)
# for i in go_visited:
#     way[i]

#각 도로에 고유키를 가지게하고, 맵핑된 고돌라의 도로에 각각의 시간을 분배하기 ,
#고돌라 먼저 출발한 뒤 각각 노드의 출발 , 이탈시간 방문리스트 만들기,

#다익스트라로 각 노드의 최소 가중치의 길로 방문& 고돌라의 시간과 겹치지 않는길로 이동 

