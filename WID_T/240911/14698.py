import sys,heapq

input= sys.stdin.readline

T = int(input())


for __ in range(T):
    power =1
    n= int(input())
    ss = list(map(int,input().split()))
    heapq.heapify(ss)

    while len(ss) > 1:
        a = heapq.heappop(ss)
        b = heapq.heappop(ss)
        power*= (a*b)
        heapq.heappush(ss,(a*b))

    print(power%1000000007)
