
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

for i in range(1,n+1):
    new_count = dfs(i)
    max_count = max(max_count, new_count) # 최댓값 구함
    result_list.append((i, new_count)) # 노드 번호별 count 값 저장
    # if max_count<new_count:
    #     max_count=new_count
    #     result_list=[i]
    # elif max_count==new_count:
    #     result_list.append(i)
for i in result_list:
    if i[1] == max_count: # 만약 count 값이 최댓값과 같다면
        print(i[0], end = ' ') # 해당 노드 번호 출력

# result_list.sort()
# print(*result_list)



      

        
    
    