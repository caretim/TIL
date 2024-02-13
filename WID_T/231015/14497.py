import heapq
import sys

input= sys.stdin.readline

INF = sys.maxsize

n,m = map(int,input().split())

y1,x1,y2,x2 = map(int,input().split())

y1-=1
x1-=1
y2-=1
x2-=1

matrix = [list(input()) for __ in range(n)]


dy,dx = [0,0,1,-1],[1,-1,0,0]



def wave(y1,x1):
    visit = [[INF for __ in range(m)] for __ in range(n)]
    visit[y1][x1] = 0
    heap = []
    heapq.heappush(heap,(0,y1,x1))
    while heap:
        cnt,y,x = heapq.heappop(heap)
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if matrix[ny][nx] =='0' and visit[ny][nx]>cnt:
                    visit[ny][nx]= cnt
                    heapq.heappush(heap,(cnt,ny,nx))
                elif matrix[ny][nx]=='1' and visit[ny][nx]>cnt+1:
                    visit[ny][nx]=cnt+1
                    heapq.heappush(heap,(cnt+1,ny,nx))
                elif matrix[ny][nx]=='#':
                    print(cnt+1)
                    exit()

wave(y1,x1)


                


            



    