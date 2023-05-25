import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


n, m = map(int, input().split())
n, m = n - 1, m - 1


graph = [[INF] * (n) for __ in range(m)]
