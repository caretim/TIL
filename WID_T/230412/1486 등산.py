import heapq

import sys

input = sys.stdin.readline


def check_high(alp):
    if alp.isupper():  # 대문자일때는A값에서 빼주기,
        return ord(alp) - ord("A")
    else:  # 소문자는 a값에서 뺴주기 ,
        return ord(alp) - ord("a") + 26


INF = sys.maxsize


N, M, T, D = map(int, input().split())
# T는 이동 할 수 있는 높이, D는 어두워지는시간,
mountain = [list(map(check_high, input().split())) for __ in range(N)]

matrix = [[INF] * (M) for _ in range(N)]

time = []

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def dijkstra(y, x):
    q = []
    matrix[y][x] = 0
    heapq.heappush(q, (0, y, x, 0))
    while q:
        t, heapq.heappop(q)
