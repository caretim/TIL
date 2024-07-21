import sys
import heapq 


input = sys.stdin.readline


n = int(input()) 
heap =[]

for i in range(n):
    num = int(input())
    heapqpush(heap,num)
    print(n/2)
    print(heap[n//2])




