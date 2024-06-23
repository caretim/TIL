import sys
input =sys.stdin.readline


n = int(input())

def move(cnt,cakes,yesterday):
    global answer
    if cnt == n:
        for d in cakes:
            print(d)
        exit()
    for cake in days[cnt]:
        if cake != yesterday and not ate[cnt][cake-1]:
            ate[cnt][cake-1] = True
            move(cnt+1, cakes + [cake],cake)

days = []
answer = []
for _ in range(n):
    m,*cake = map(int, input().split())
    days.append(cake)
ate = {i:[False for _ in range(10)] for i in range(n+1)}
move(0,[],0)
print(-1)