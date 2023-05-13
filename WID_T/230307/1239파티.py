import sys
import heapq


#각 노드에서 시작해서 x마을찍고 돌아오는 거리 계산, 

# 출발해서 다시 x에서 처음으로 돌아오는거 다익 2번 돌리기 

input=sys.stdin.readline

N,M,X = map(int,input().split())

INF = sys.maxsize



result=[0]*(N+1)

heap = []

def dijkstra(start,end):
    vil = [INF]*(N+1) # 각 마을의 학생 이동거리
    vil[start] = 0  # 근데, 노드에서, 시간..X에 도착했을 경우? 
    # 직전노드에서, X를 도착하는 방법, 흠,, 각 지점을 트래킹해서 지정해놓기? 
    # 한번 돌면 연결된 노드로는 최소시간이 지정되는건 동일함,
    # 시간 줄여주려면, 노드 이동 경로 체크? 다른길에서는 더 빠르게 올 수도 있구나,
    # 아니네 방향은 어차피 단방향이라, 의미가 없음 
    # 생각해보니까 그냥 앞에들어가는 출발노드 마지막노드 바꿔서 두번 돌리면 되겠다
    heapq.heappush(heap,(0,start))
    while heap:
        wei, node = heapq.heappop(heap)

        if vil[node] < wei:
            continue

        for w,next_node in graph[node]:
            next_wei= w+wei

            if next_wei<vil[next_node]:
                vil[next_node]= next_wei
                heapq.heappush(heap,(next_wei,next_node))

    return vil[end]

graph = [[] for __ in range(N+1)]

for __ in range(M):
    u,v,w= map(int,input().split())
    graph[u].append((w,v))


for k in range(1,N+1):
    result[k]= dijkstra(k,X) + dijkstra(X,k)

print(max(result))

