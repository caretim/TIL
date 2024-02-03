import sys
from collections import deque

input =sys.stdin.readline

INF = sys.maxsize
# 연결된 건물이 모두 완성되어야 현재 건물 건설 가능

# 직전노드에서 가장 오래걸렸던 시간 + 본인시간

for tc in range(int(input())):

    n,k = map(int,input().split())

    arr = list(map(int,input().split()))

    visited= [[0 for __ in range(n)] for __ in range(n)]  # 방문확인

    graph = [[] for __ in range(n)] # 

    check_graph = [0]*n # 방문 빌드 완성 확인


    for __ in range(k):
        x,y = map(int,input().split())
        graph[x-1].append(y-1)
        check_graph[y-1]+=1
        



    target = int(input()) -1

    build_time = [-1] * n
    q = deque()
    for i in range(n):
        if check_graph[i]==0:
            q.append((i,arr[i]))
            visited[i][i] = 1
            build_time[i] = arr[i]
    
    while q:
        node,time = q.pop()
        if node == target:
            print(time)
            break
        for next_node in graph[node]:
            next_time = time+arr[next_node] #기본적으로 하위건물이 완성되어야 q에 추가가능
            if visited[next_node][node] ==0:
                visited[next_node][node]=1
                check_graph[next_node] = check_graph[next_node]-1  # 본인 노드 체크 개수 확인 
                if build_time[next_node]<next_time:
                    build_time[next_node] = next_time
                if check_graph[next_node]==0:
                    q.appendleft((next_node,build_time[next_node]))


