import sys 

from collections import deque

input = sys.stdin.readline

INF = sys.maxsize
 
n = int(input())


graph = [ [ ] for  __  in range(n+1)]

while True:
	u,v= map(int,input().split())
	if (u,v) == (-1,-1):
		break
	graph[u].append(v)
	graph[v].append(u)
	
def bfs(start) :	
	visited=[INF]*(n+1)
	visited[0]=0
	q = deque()
	visited[start]=0
	q.append(start)
	
	while q:
		node = q.pop()
		for i in graph[node]:
			if visited[i]  > visited[node]+1:
				visited[i]= visited[node]+1
				q.append(i)		
	return max(visited)
	



result_node=[]
min_cnt =INF

for i in range(1,n+1):
		now_cnt = bfs(i)
		if min_cnt>now_cnt:
			min_cnt = now_cnt
			result_node =[i]
		elif min_cnt==now_cnt:
			result_node.append(i)
		
		
print(min_cnt, len(result_node))

print(*result_node)
