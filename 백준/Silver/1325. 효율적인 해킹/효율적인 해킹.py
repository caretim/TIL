
import sys

input =sys.stdin.readline


n,m= map(int,input().split())


graph =[[] for __ in range(n+1)]

for __ in range(m):
    u,v = map(int,input().split())
    graph[v].append(u)



def dfs(a):
    arr = [0]*(n+1)
    arr[a] = 1
    q=[]
    q.append(a)
    cnt = 0 
    while q:
        node = q.pop()
        for next_node in graph[node]:
            if arr[next_node]==0:
                arr[next_node]=1
                cnt+=1
                q.append(next_node)
    return cnt 

result_list = []
max_count = -1

for i in range(n+1):
    new_count = dfs(i)
    if max_count<new_count:
        max_count=new_count
        result_list=[i]
    elif max_count==new_count:
        result_list.append(i)


result_list.sort()
print(*result_list)



      

        
    
    