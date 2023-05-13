
from collections import deque

A,B = map(int,input().split())

# check = [0]* (B+1)


q=deque()
q.append((A,0))

result = -1 
while q:
    n,j= q.popleft()
    j+=1
    if n == B:
        result = j
        break # 횟수더하는 위치 생각 
    if len(str(n))<= len(str(B)):
        for i in n*2,((n*10)+1):
            if 0<=i<=B :
                # check[i]=j
                q.append((i,j))
    else:
        for i in n*2:
            if 0<=i<=B :
                # check[i]=j
                q.append(i,j)
        
print(result)
            