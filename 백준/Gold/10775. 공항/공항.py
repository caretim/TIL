import sys
input =sys.stdin.readline


g= int(input())
p =int(input())

root=[]
       
def find(node):
    if root[node] ==node:
        return node
    else:
        while root[node]!=node:
            node= root[node]
            root[node] = root[root[node]]
        return node
    

for i in range(g+1):
    root.append(i)

land = []

for __ in range(p): # 각각 비행기 착륙
    land.append(int(input()))

result = 0


for i in land:
    c = find(i)
    if c == 0:
        break
    root[c] = c-1
    result+=1


print(result)