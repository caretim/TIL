n,m =map(int,input().split())
graph =[[0]*(n+1) for __ in range(n+1)]

graph[0][0]=1

for i in range(0,n+1):
    for j in range(n+1):
        if j == 0 :
            graph[i][j]=1
        else:
            graph[i][j]= graph[i-1][j-1]+graph[i-1][j]

print(graph)
print(graph[n-1][m-1])