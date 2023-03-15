
import heapq 
import sys
input= sys.stdin.readline



n= int(input())
x =[ ]

for __ in range(n):
    inp = int(input())
    if inp == 0:
        if len(x)>0:
            print(heapq.heappop(x),'답')
        else:
            print(0,'답')
    else:
        heapq.heappush(x,inp)