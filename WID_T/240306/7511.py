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
t = int(input())
for i in range(t):
    print(f'Scenario {i+1}:')
    n = int(input())
    root = [j for j in range(n)]
    k = int(input())
    
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    m = int(input())

    for _ in range(m):
        u, v = map(int, input().split())
        p1 = find(u)
        p2 = find(v)
        if p1 == p2:
            print(1)
        else:
            print(0)
    print()