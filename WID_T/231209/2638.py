import sys
from collections import deque

input = sys.stdin.readline

INF = sys.maxsize


# 외부공기 -1 ,
# 내부공기 0 ,
#


n, m = map(int, input().split())


dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


matrix = [list(input().rstrip()) for __ in range(n)]

visited = [[0] * (m) for __ in range(n)]
