import sys


input = sys.stdin.readline

n = int(input())

values = list(map(int, input().split()))


mv, r = 0, 0
for i in range(n - 1, -1, -1):
    mv = max(mv, values[i])
    r = max(r, mv - values[i])

print(r)
