import sys
import heapq


input = sys.stdin.readline


n = int(input())

score = []

max_day = 0
for __ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(score, (-w, d))
    if max_day < d:
        max_day = d


check = [0] * (max_day + 1)

print(score)
day = 0
result = 0
while score:
    w, d = heapq.heappop(score)
    print(w)
    w = -w
    for i in range(d, 0, -1):
        if check[i]:
            continue

        check[i] = 1
        result += w
        break


print(result)
