import sys


input = sys.stdin.readline

n = int(input())
k = int(input())

visited = [[0]*(21) for __ in range(n+1)]

aclist= []*(n+1)

def ironMove(move,tree):
    move = set(move)
    ac = []
    while move:
        now = move.pop()
        for i in (0,1,-1,now):
            next = now +i
            if next >20:
                next =20
            if next <1:
                continue
            if visited[tree][next]==1:
                ac.append(next) 
    return ac
# 가만히 있는 o기능,
# 위로 1m 이동하는 A기능,
# 현재 높이만큼 위로 이동하는 B기능 (만약 현재 높이가 10m 이상이라면 항상 20m로 이동)
# 아래로 1m 이동하는 C기능
# 위 아래 어느 위치로든 순간이동 할 수 있는 T기능을 갖고 있다

for i in range(n):
    mv = list(map(int,input().split()))
    aclist.append(mv[1:])
    for j in range(mv[0]):
        visited[i][mv[j+1]] = 1

result = 0
now =1
move =[1]
for i in range(n):
    nextmove = ironMove(move,i)
    move= nextmove
    if not nextmove:
        result+=1
        if result > k:
            result= -1
            break
        move = aclist[i]
        

print(result)
    






