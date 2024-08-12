import sys

import heapq
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
n =int(input())


matrix = [[]for __ in range(n)]

early =[0] *n

node_Cnt = [[0,0] for i in range(n)]

# 현재노드에서 다른노드로 이동되는 노드는 얼리가 되어야함, 

#본인을 제외한 인자는 모두 얼리어야함

# 모든 노드를 순회하는건 시간초과, 

#1.가장 많은 원소를 가진 노드부터 얼리적용, 
#2.다음 노드의 패스가 현재 노드밖에 존재하지 않는다면 현재 노드는 얼리가 되어야함, 
#1)heap으로 가장 큰 노드를 가진 원소부터 탐색, 
#
for __ in range(n-1):
    u,v = map(int,input().split())
    u-=1;v-=1
    matrix[u].append(v)
    matrix[v].append(u)


## 실패  -> 완전탐색 시간초과
# while node_Cnt:
#     node = heapq.heappop(node_Cnt)
#     node= node[1]
#     for k in matrix[node]:
#         if early[k]==0:
#             early[node]=1
#             break

# print(sum(early))

def dfs(node):
    early[node] = 1
    node_Cnt[node][1] = 1
    for i in matrix[node]:
        if not early[i]:
            dfs(i)
            node_Cnt[node][1] += min(node_Cnt[i][0],node_Cnt[i][1])
            node_Cnt[node][0] += node_Cnt[i][1]
dfs(1)
print(min(node_Cnt[1][0],node_Cnt[1][1]))