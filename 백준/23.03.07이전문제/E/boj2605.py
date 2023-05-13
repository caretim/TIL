# 

n= int(input())

jool= []

k = list(map(int,input().split()))

for st in range(n):
    
    if k[st] == 0:
        jool.append(st+1)
    elif k[st]>= 1:
        jool.insert(len(jool)-k[st],st+1)

print(*jool)