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


for _ in range(int(input())):
    n = int(input())
    m = int(input())
    root = [i for i in range(n + 1)]
    result = 'tree'
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            result = 'graph'
        else:
            union(a, b)
    x = find(1)
    for i in range(2, n + 1):
        if x != find(i):
            result = 'graph'
    print(result)