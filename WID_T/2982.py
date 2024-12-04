import sys, heapq

input = sys.stdin.readline


INF = sys.maxsize

n,m= map(int,input().split())

#A는 상근이가 배달을 시작하는 교차로,
#B는 상근이가 배달을 마치는 교차로이다. 
#K는 고둘라가 출발한 시간과 상근이가 출발한 시간의 차이, 
#G는 고둘라가 방문하는 교차로의 개수이다
A, B, K, G =  map(int,input().split())

#G개의 정수가 주어진다.이 정수는 고둘라가 방문하는 교차로
gd = list(map(int,input().split()))


graph =[[] for __ in range(n)]

for __ in range(m):
    u,v,