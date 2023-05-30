
import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

dy,dx = [0,0,1,-1],[1,-1,0,0]



def dijkstra(sx,sy):
    check =[[INF]*(w) for __ in range(h)]
    check[sx][sy]= 0
    q=[]
    heapq.heappush(q,(0,sx,sy))
    while q:
        co,x,y, = heapq.heappop(q)
        if check[x][y]<w:
            continue
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<h and 0<=ny<w :
                cost =co+matrix[nx][ny]
                if check[nx][ny]>cost:
                    check[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny))
                    print('힙 넣음')
            else:
                return check[x][y]

    



k,w,h = map(int,input().split())

battle_class = {}





for __ in range(k):
    cla,cost = input().split()
    battle_class[cla]=int(cost)

battle_class['E'] =0
# 최조 E 시작점 지정 

def transform(char):
    res = battle_class[char]
    return res

matrix= [list(map(transform,input().rstrip())) for __ in range(h)]


for y in range(h):
    for x in range(w):
       if  matrix[x][y] ==0:
           sx =x
           sy=y

 

print(dijkstra(sx,sy))




