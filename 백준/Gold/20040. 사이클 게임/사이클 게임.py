

import sys
sys.setrecursionlimit(100001)
input =sys.stdin.readline



n,m= map(int,input().split())

root ={}


for i in range(n):
    root[i] = i

def find_root(node):
    if root[node] == node:
        return node
    while node != root[node]:
        node = root[node]
        root[node] = root[root[node]]
    return node

def union(x,y):
    a= find_root(x)
    b= find_root(y)

    if a!=b:
        root[b] = a
        return False
    elif a==b:
        return True
    



for i in range(m):
    x,y = map(int,input().split())
    if union(x,y):
        print(i+1)
        exit()

print(0)











