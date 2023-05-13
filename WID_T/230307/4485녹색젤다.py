import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

count =0
while True:
    count+=1
    n= int(input())
    if n == 0:
        break

    matrix =[list(map(int,input().split())) for __ in range(n)]



    check_matrix= [[INF]*(n) for __ in range(n)]

    dy,dx= [0,0,1,-1],[1,-1,0,0] 


    def dijkstra(y,x):
        q =[]
        check_matrix[y][x] =matrix[y][x]
        heapq.heappush(q,((matrix[y][x],y,x)))
        while q:
            j,y,x= heapq.heappop(q)
            if j>check_matrix[y][x]:
                continue
            for i in range(4):
                ny,nx= y+dy[i],x+dx[i]
                if 0<=ny<n and 0<=nx<n:
                    if j+matrix[ny][nx] <check_matrix[ny][nx]:
                        check_matrix[ny][nx]= j+matrix[ny][nx]
                        heapq.heappush(q,(check_matrix[ny][nx],ny,nx))


    dijkstra(0,0)
    print(f'Problem {count}: {check_matrix[n-1][n-1]}')
