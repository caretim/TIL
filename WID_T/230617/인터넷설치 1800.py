import sys
import heapq
import copy

INF = sys.maxsize
input = sys.stdin.readline

N, M ,K= map(int, input().split())

graph = [[] for __ in range(N + 1)]




for i in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))



#다익스트라를 통해서 mid값(비용의 최대한계)이내에서 통과가 되는지 확인시켜주기,
# k번의 최대값 패스권 사용 max_v는 mid값  

def dijkstra(s,max_v,k):  
    arr=[INF] *(N+1) # 노드마다 패스권을 사용한 기준으로 확인하기,
    q =[]
    heapq.heappush(q,(0,s))
    arr[s]=0
    while q:
        cnt,node= heapq.heappop(q)
        if cnt>k: # 최대카운트를 넘어간다면 컨틴뉴, 굳이 안넣어도 될듯,
            continue
        if node == N: # k 카운트 안에 목표 도달 시  True 리턴
            return True
        for wei,next_node in graph[node]:
            if wei > max_v and cnt<k:
                if arr[next_node]>cnt+1:
                    arr[next_node]=cnt+1
                    heapq.heappush(q,(cnt+1,next_node))

            elif wei<=max_v :
                if arr[next_node]>cnt:
                    arr[next_node]=cnt
                    heapq.heappush(q,(cnt,next_node))
    return False
        
# 어차피 비용은 백만 이하, 
# 비용을 기준으로 이분탐색을 진행
# 이분탐색을 넣어 True로 이어지는 부분을 확인해서 사용 , 
# mid를 다익스트라에 넣어서 True가 되는 최솟값이 답이 된다,

#만일 그냥 그리디를 통해 비용 최대값을 넣어서 진행하게되면 시간초과 발생,

#이분탐색을 통해 True가 나오는 mid의 최소값을 확인한다.

left, right = 0, 1000001
result = INF
while left <= right:
    mid = (left + right) // 2
    flag = dijkstra(1,mid,K)
    if flag:
        right = mid - 1
        result = mid

    else:
        left = mid + 1

if result ==INF:
    print(-1)
else:
    print(result)



    





