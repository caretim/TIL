from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

commit_matrix = [list(map(int, input().split())) for __ in range(n)]

origin_check = [[0]*m for __ in range(n)]

# while cnt = 0일때까지,
# 1.탐색할때 주변값이 바뀌게된다면 또 탐색하게 되므로 체크리스트 만들어줘야함,
# 2.모두 탐색했을때까지, (result 리스트안의 인자가 없다면,) 0을 출력 , 
# 3.탐색기능에 cnt를 넣어서 모두 녹았는지 0일 시 (1), 그리고 빙하의 갯수를 확인
# 4. 빙하하나당 4방탐색 진행해줘야함,  그리고 탐색하는 값은, 큐에 들어가게되고 , 


def bfs(y,x):
    q=deque()
    q.append((y,x))
    while q:
        g = q.popleft()
        bada=0
        for i in range(4):
            ny= g[0] + dy[i]
            nx= g[1] + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if commit_matrix[ny][nx] == 0:
                    bada+=1
                if commit_matrix[ny][nx] > 0 and check[ny][nx] == 0:
                    q.append((ny,nx))
                    check[ny][nx]=1
        matrix[g[0]][g[1]]-= bada
        if matrix[g[0]][g[1]] < 0:
            matrix[g[0]][g[1]] = 0


cnt=0      # 년수 세어주는 카운터 
while True:
    bingsan = 0  # 녹고나서 빙산이 몇개로 갈라지는지 카운트 
    matrix= deepcopy(commit_matrix)
    check = deepcopy(origin_check)
    for y in range(n):
        for x in range(m):
            if matrix[y][x]>=1 and check[y][x]==0:
                check[y][x]=1
                bingsan+=1
                bfs(y,x)
    cnt+=1
    if bingsan > 1:
        print (cnt-1)
        break
    elif bingsan == 0:
        print ('0')
        break
    commit_matrix=matrix
    
    
    



    

#     def 한번 실행할떄 높이 -1씩  

#     깍고나서 빙산쪼개졌는지 안쪼개졌는지 확인 ,

#     for y in range(m):
#         for x in range(n):
            
#             각각의 매트릭스 
            
#              빙산들 안의 높이를 한번 돌때 사방의 0의 숫자를 카운트해서 좌표값의 높이를 1씩 빼줌)

#             (-> 그리고 탐색했을때 각각 빙산들의 주변 사방을 델타탐색을 통해서 0의 숫자를 카운트하고 -> 높이를 줄여줍니다.

#             이걸 하면서 동시에, 방문처리 한번의 그래프 탐색을 할때 각각 방문위치를 기록해줘야함. ) 

# 해당 좌표의 상하좌우 빈공간바다 (0) 가 존재할 경우 매년 빙산의 길이가  -

# 4방위 델타탐색을 해야하는데, 먼저 저희가 구해야 할 부분은 , 빙산이 두개로 쪼개는 순간이 언제인지 확인을해야함,
#-> 빙산  두개 쪼개지는것 , 그리고 시간이 흐르면서 빙산의 높이가 줄어드는것을 생각해야함, 