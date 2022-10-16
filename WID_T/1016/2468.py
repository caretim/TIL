from collections import deque
from copy import deepcopy
from pprint import pprint

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(input())


matrix = [list(map(int, input().split())) for __ in range(n)]


# 먼저 매트릭스 범위중 제일 큰 값 찾기

# 0~제일 큰 값 범위 확인 후 for문으로 탐색 진행 ,

result = []


def bfs(y, x, rain):  # y,x 좌표값과 강수량 rain을 가져온다.
    check[y][x] = -1  # 방문좌표 체크는 -1로 표시  (양수만 체크됨으로 음수로 체크하기 )
    q = deque()
    q.append((y, x))
    while q:  # 강수량 rain의 높이보다 큰 영역을 델타탐색으로 탐색해준 후  탐색한 장소는 -1로 방문표시
        k = q.popleft()
        for j in range(4):
            ny = k[0] + dy[j]
            nx = k[1] + dx[j]
            if 0 <= ny < n and 0 <= nx < n:
                if check[ny][nx] > rain:
                    check[ny][nx] = -1
                    q.append((ny, nx))


max_vlaue = max(map(max, matrix))   # max_value은 최대 강수량 받는 입력 범위중 가장 큰 값을 확인, 

for rain in range(0, max_vlaue):     # 0 = 비가안올때, max_vlaue = 최고치로 비가 내릴 때  비가 안올 때 부터 최고치로 비가 내리는 범위까지 모두 탐색 
    check = deepcopy(matrix)         # matrix를 여러번 참조해서 사용해야하는데 그냥 check= matrix를 하게되면 얕은복사게 되어서 깊은복사를 하기위해 deepcopy사용
    cnt = 0
    for y in range(n):
        for x in range(n):
            if check[y][x] > rain:   
                cnt += 1            # 높이별 탐색 중 안잠긴 영역을 확인해서 . 카운트 해준다.
                bfs(y, x, rain)

    result.append(cnt) # 강수량별 안전영역을 result 리스트에 넣어준다.

print(max(result))  # 강수량별 안전영역을 넣어준 리스트중에 가장 안전영역이 넓은 곳을  출력 
