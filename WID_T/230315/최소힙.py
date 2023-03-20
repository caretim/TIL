import heapq
import sys

input = sys.stdin.readline


n = int(input())
x = []

for __ in range(n):
    inp = int(input())
    if inp == 0:
        if len(x) > 0:
            i, j = heapq.heappop(x)
            print(j)
        else:
            print(0)
    else:
        heapq.heappush(x, inp * -1, inp)
