# 좌표 정렬하기 boj 11650.py

import heapq
import sys

n=int(input())


nl = []

heapq.heapify(nl)

for __ in range(n):
    x,y=sys.stdin.readline().rstrip().split()
    heapq.heappush(nl,(int(x),int(y)))

for __ in range(n):
    result= heapq.heappop(nl)
    print(*result)




