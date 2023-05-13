import sys
import heapq











n= int(input())
a,b,c= map(int,input().split())

m= int(input())

graph = [[] for __ in range(n)]

for __ in range(m):
    graph