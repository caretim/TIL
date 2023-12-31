import heapq
import sys


input = sys.stdin.readline

n = int(input())

present = []

result = []
for __ in range(n):
    add = list(map(int, input().split()))
    if add[0] == 0:
        if len(present) > 0:
            print(-(heapq.heappop(present)))
        else:
            print(-1)
    else:
        for i in range(add[0]):
            heapq.heappush(present, -(add.pop()))
