import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 값이 이동할 떄 이동하기전의 값을 미리 넣어준다.

check = [0] * 100001
move = [0] * 100001


n, k = map(int, input().split())

q = deque()


def bfs(n, k):
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return
        for i in (x + 1, x - 1, x * 2):
            if 0 <= i < 100001 and check[i] == 0:
                check[i] = check[x] + 1
                move[i] = i
                q.append(i)
    print(move)


def tracking(n, k):
    if n != k:
        tracking(n, move[k])
    print(k, sep=" ")


print(check[k])

tracking(n, k)
