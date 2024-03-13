import sys
from collections import deque
input =sys.stdin.readline

n,m= map(int,input().split())

root = [i for i in range(n)]

def find(node):
    if node == root[node]:
        return node
    else:
        while node != root[node]:
            node= root[node]
            root[node] = root[root[node]]
        return node

def union(x,y):
    a= find(x)
    b= find(y)

    if a!=b:
        root[b] = root[a]
        return False
    else:
        return True



for __ in range(m):
    a,b = map(int,input().split())
    union(a,b)




