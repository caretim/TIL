import sys,heapq


input = sys.stdin.readline

n= int(input())

result=[]

high = []

for __ in range(n):
    x,h,y = map(int,input().split())
    heapq.heappush(high,(x,h))
    heapq.heappush(high,(y,h))

now = 0

prevhigh = 0
while heapq and now>heapq[0][1]:

#높이가 변하는순간 기록,
# 현재 높이와 위치 ,


