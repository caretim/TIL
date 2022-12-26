from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())


matrix = [(list(map(int,input().split()))) for __ in range(n)]


dy = [0,0,1,-1]
dx = [-1,1,0,0]



result=[] # 각 섬마다 제일 가까운 곳 연결되는위치 저장리스트 


# 섬 번호 바꿔주는 dfs 
def dfs(y,x):
    matrix[y][x]=i_count
    q = []
    q.append((y,x))
    while q:
        k = q.pop()
        for i in range(4):
            ny = k[0]+dy[i]
            nx = k[1]+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if matrix[ny][nx] == 1:
                    matrix[ny][nx]= i_count
                    q.append((ny,nx))

# 체크리스트 생성 후 bfs탐색  튜플로 (y,x,거리)
def bfs(j):
    check = [[-1]*n for __ in range(n)] #체크리스트 본인섬이 아닐 시 기본 -1 지정  내륙일경우 0으로지정  
    q = deque()
    for y in range(n):
        for x in range(n):   # 섬의번호와 같은 위치 모두 0으로 변경  , 주변에 바다가 있다면 큐에 넣어주기 
            if matrix[y][x] == j:
                check[y][x] = 0 
                for i in range(4):
                    ny=y+dy[i]
                    nx=x+dx[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if matrix[ny][nx]==0:
                        q.append((y,x))
                        continue
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            #섬을 찾았을 경우 0은 바다 , j는 시작섬 제외
            if matrix[ny][nx]>0 and matrix[ny][nx]!=j:
                return check[y][x]
            #바다에서 방문을 안했을 경우
            if matrix[ny][nx]==0 and check[ny][nx]==-1:
                check[ny][nx]=check[y][x]+1
                q.append((ny,nx))
    
# 기본 매트릭스에서 섬의 갯수 체크 
i_count=1
for y in range(n):
    for x in range(n):
        if matrix[y][x] == 1:
            i_count+=1
            dfs(y,x)


# 섬의 번호 번호가 일치하면 bfs 탐색 

for j in range(2,i_count+1):
    ans = False
    for y in range(n):
        if ans == True:
            break
        for x in range(n):
            if matrix[y][x] == j:
                re = bfs(j) 
                result.append(re)
                ans=True
                break


print(min(result))

