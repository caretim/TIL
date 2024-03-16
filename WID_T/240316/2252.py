from collections import deque
import sys


input=sys.stdin.readline
n,m=map(int,input().split())
degree=[[] for _ in range(n+1)]
num=[0 for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    degree[a].append(b)
    #degree[b]=a
    num[b]+=1

queue=deque()
for i in range(1,n+1):
    if num[i]==0:
        queue.append(i)

result=[]
while queue:
    cu=queue.popleft()
    result.append(cu)
    for i in degree[cu]:
        num[i]-=1
        if num[i]==0:
            queue.append(i)
print(*result)