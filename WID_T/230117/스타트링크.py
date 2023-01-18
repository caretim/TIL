from collections import deque

F, S, G, U, D = map(int, input().split())
# 총 F층으로 이루어진 고층 건물에 사무실이 있고,
#  스타트링크가 있는 곳의 위치는 G층이다. 강호가 지금 있는 곳은 S층이고,
#  이제 엘리베이터를 타고 G층으로 이동하려고 한다
check = [-1] * (F + 1)

UD = [U, -D]


def bfs(s):
    check[s] = 0
    q = deque()
    q.append((s, 0))
    while q:
        k, m = q.popleft()
        for i in range(2):
            move = k + UD[i]
            if 0 < move <= F and check[move] == -1:
                check[move] = m + 1
                q.append((move, m + 1))


bfs(S)
print(check)
if check[G] == -1:
    print("use the stairs")
else:
    print(check[G])
