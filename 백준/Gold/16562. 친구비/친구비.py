import sys

input =sys.stdin.readline

n,m,k= map(int,input().split())

fp = list(map(int,input().split()))

root =[]


def root_find(node):
    
    if root[node] ==node:
        return node
    
    while root[node]!=node:
        root[node] = root[root[node]]
        return root[node]

def union(x,y):
    a = root_find(x)
    b = root_find(y)

    if root[a]!=root[b]:
        root[b] = root[a] = min(root[a],root[b])
        fp[a]=fp[b] = min(fp[a],fp[b])


for i in range(n):
    root.append(i)


for __ in range(m):
    u,v =map(int,input().split())
    u-=1
    v-=1
    union(u,v)

for o in range(n):
    root_find(o)

pay = 0
for i in set(root):
    pay+=fp[i]


if k >= pay:
    print(pay)
else:
    print('Oh no')