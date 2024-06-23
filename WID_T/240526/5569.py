import sys
sys.setrecursionlimit(10 ** 5)



def tracking(now, day):
    if day == n:
        for i in range(1, n + 1):
            print(visited[i])
        sys.exit(0)

    for nxt in cakes[day + 1]:
        if nxt != now and not check[nxt][day + 1]:
            check[nxt][day + 1] = True
            visited[day + 1] = nxt
            tracking(nxt, day + 1)
    return

n = int(input())

cakes = dict()

check = [[False] * (n + 1) for _ in range(10)]

for i in range(1, n + 1):
    m, *a = map(int, input().split())
    cakes[i] = a

for x in cakes[1]:
    if not check[x][1]:
        check[x][1] = True
        visited = [0] * (n + 1)
        visited[1] = x
        tracking(x, 1)

print(-1)
