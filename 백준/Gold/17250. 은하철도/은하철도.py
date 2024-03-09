import sys 
input =sys.stdin.readline



n,m= map(int,input().split())

root = [i for i in range(n)]

star = []


for __ in range(n):
    star.append(int(input()))


def find(node):
    if root[node]==node:
        return node
    else:
        while root[node]!=node:
            node = root[node]
            root[node] = root[root[node]]
        return node 



def union(x,y):
    a= find(x)
    b= find(y)
    if a!=b:
        root[b]= a
        star[a]+= star[b]
        print(star[a])
    elif a==b:
        print(star[a])



for __ in range(m):
    x,y = map(int,input().split())
    x-=1
    y-=1
    union(x,y)

    
