import sys

imput =sys.stdin.readline

n= int(input())

if n <=2:
    print(1,2)
    exit()


visit = [0]*(n)
root={}

def find(node):
    if root[node] ==node:
        return node
    else:
        while root[node]!=node:
            node= root[node]
            root[node] = root[root[node]]
        return node


result=set()

def union(x,y):
    a = find(x)
    b = find(y)
    if a!=b:
        root[b]=root[a]


for i in range(n):
    root[i] =i 

for __ in range(n-2):
    x,y = map(int,input().split())
    x-=1
    y-=1
    visit[x]=1
    visit[y]=1
    union(x,y)

for i in range(n):
    result.add(find(i))



if len(result)==2:
    for i in result:
        print(i+1,end=' ')
elif len(result)==1:
    print(visit.index(0)+1,result.pop()+1)




