
import sys
input =sys.stdin.readline
sys.setrecursionlimit(100001)
root ={}


def find_Root(node):
    if node == root[node]:
        return node
    else:
        root[node] = find_Root(root[node])
        return root[node]
    
def union(x,y):
    a = find_Root(x)
    b = find_Root(y)

    if a!=b:
        root[b] = a


n,m= map(int,input().split())

for i in range(0,n+1):
    root[i]= i


for __ in range(m):
    o,x,y = map(int,input().split())
    if o:
        if find_Root(x) == find_Root(y):
            print("YES")
        else:
            print("NO")
    else:
        union(x,y)