import sys

input = sys.stdin.readline


def find(node):
    if root[node] ==node:
        return node
    else:
        while root[node]!=node:
            node= root[node]
            root[node] = root[root[node]]
        return node

def union(x,y):
    a = find(x)
    b = find(y)
    if a!=b:
        root[b]=root[a]

n,m =map(int,input().split())

root=[i for i in range(n+1)]


for __ in range(m):
    a,b= map(int,input().split())
    union(a,b)


for i in range(n):
    find(i)


classtime = list(map(int,input().split()))

now= classtime[0]

cnt = 0

for i in range(1,len(classtime)):
    if find(now) != find(classtime[i]):
        cnt+=1
        now = classtime[i]
print(cnt)