import sys

input = sys.stdin.readline


n, m = map(int, input().split())


dict = {}
result = []

for i in range(1, n + 1):
    result.append(i)
    dict[i] = i

for __ in range(m):
    a, b = map(int, input().split())

    result.insert(result.index(b), a)
