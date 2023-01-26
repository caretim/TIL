import sys

input= sys.stdin.readline

n,m = map(int,input().split())

node =[[] for __ in range(n)]


check=[0]*n

for __ in range(m):
    i,j=map(int,input().split())
    node[i].append(j)

print(node)
def dfs(x): #본인까지 돌아오는지 체크해야함, 
    stack = []
    stack.append(x)
    check[x]=1
    while stack:
        k = stack.pop()
        for i in node[k]:
            if check[i]==0:
                stack.append(i)
                check[i]=1
dfs(0)

print(check)
result = 1
for r in check:
    if r==0:
        result = 0

print(result)


