import sys
import heapq


input =sys.stdin.readline
n,m =map(int,input().split())


matrix =[set() for __ in range(n+1)]
check_node =[set() for __ in range(n+1)]

visit = [0]*(n+1)

result = []
# 가능한 쉬운문제부터 먼저 , 연산 진행되며 지나가는 노드전에 
# 재귀형식 ㄴㄴ 선형구조로 풀어야함, 각 연산 연결 포인터로 연결 

# def solve(node): 
#     if visit[node]:
#         return

#     next=matrix[node]
#     heapq.heapify(next)
#     while next:
#         next_node = heapq.heappop(next)
#         solve(next_node)
#     visit[node]=1
#     result.append(node)
#     return

def sol_node(node,old_node):

    if visit[node]: # 방문했거나, 하위노드가 존재한다면 , 리턴 
        return
    if not matrix[node]: # 하위노드가 비어있다면 추가작업 진행
        result.append(node) # 탐색 후 방문체크
        visit[node]=1 # 연산 순서 res에 현재노드 추가
        while check_node[node]: # 현재 노드를 하위노드로 가지고 있는 노드(상위노드)탐색
            i = min(check_node[node])
            print(i,matrix[i],f'올드노드{old_node}')
            check_node[node].remove(i)
            matrix[i].remove(node) # 상위노드의 하위노드에 현재노드 제거
            if old_node>i and not matrix[i]: # 현재 노드 값 보다 상위노드 값이 작다면
                sol_node(i,old_node) #제거 후 상위노드의 하위노드가 없다면 탐색진행 
    return

for __ in range(m):
    u,v, = map(int,input().split())
    matrix[v].add(u)
    check_node[u].add(v)



for i in range(1,n+1):
    sol_node(i,i)


print(*result)