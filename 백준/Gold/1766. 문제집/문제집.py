import sys
import heapq


# input =sys.stdin.readline
# n,m =map(int,input().split())


# matrix =[set() for __ in range(n+1)]
# check_node =[set() for __ in range(n+1)]

# visit = [0]*(n+1)

# result = []

# def sol_node(node,old_node):

#     if visit[node]: # 방문했거나, 하위노드가 존재한다면 , 리턴 
#         return
#     if not matrix[node]: # 하위노드가 비어있다면 추가작업 진행
#         result.append(node) # 탐색 후 방문체크
#         visit[node]=1 # 연산 순서 res에 현재노드 추가
#         next_nodes = []
#         while check_node[node]: # 현재 노드를 하위노드로 가지고 있는 노드(상위노드)탐색
#             i = min(check_node[node])
#             check_node[node].remove(i)
#             matrix[i].remove(node)
#             next_nodes.append(i) # 상위노드의 하위노드에 현재노드 제거
#             # print('제거되는값',(i),check_node[i],f'올드노드{old_node}')
#         for i in next_nodes:
#             if old_node>i and not matrix[i]: # 현재 노드 값 보다 상위노드 값이 작다면
#                 # print(i,'실행값')
#                 sol_node(i,old_node) #제거 후 상위노드의 하위노드가 없다면 탐색진행 


# for __ in range(m):
#     u,v, = map(int,input().split())
#     matrix[v].add(u)
#     check_node[u].add(v)



# for i in range(1,n+1):
#     sol_node(i,i)


# for r in result:
#     print(r,end=' ')




n, m = map(int, input().split())
node_cnt = [0] * (n + 1)
matrix = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    node_cnt[b] += 1
    matrix[a].append(b)

q = []

for i in range(1, n + 1):
    if node_cnt[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    print(now, end=" ")

    for g in matrix[now]:
        node_cnt[g] -= 1

        if node_cnt[g] == 0:
            heapq.heappush(q, g)