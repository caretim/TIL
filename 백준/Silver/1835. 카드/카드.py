import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
q = deque()
q.appendleft(N)

for n in range(N - 1, 0, -1):
    q.appendleft(n)

    for j in range(n):
        moveCard = q.pop()
        q.appendleft(moveCard)

print(*q)