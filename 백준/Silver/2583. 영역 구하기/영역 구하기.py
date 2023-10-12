from collections import deque


m, n, k = map(int, input().split())


matrix = [[0] * (n) for __ in range(m)]  # 매트릭스 범위 지정 

dy = [-1, 0, 1, 0] # 델타 4분탐색 좌표 지정
dx = [0, 1, 0, -1]


result = []


# m = 5세로 n=7 가로
def bfs(y, x):  # bfs를 통해 사이즈 확인 
    size = 1
    matrix[y][x] = 1
    q = deque()
    q.append((y, x))

    while q:
        k = q.popleft()
        for i in range(4):
            ny = k[0] + dy[i]
            nx = k[1] + dx[i]
            if 0 <= ny < m and 0 <= nx < n:
                if matrix[ny][nx] == 0: # 직사각형 외의 지역은 0 직사각형에 포함된 지역은 1이므로 0일시 큐에 추가해준다.
                    q.append((ny, nx)) 
                    matrix[ny][nx] = 1
                    size += 1
    return size


for __ in range(k):
    x1, y1, x2, y2 = map(int, input().split())   # 사각형의 범위를 받아준다. 
    for y in range(y1, y2):
        for x in range(x1, x2):  # 각 받아준 범위를 이중for문을 통해 표시 문제 상에서 좌표는 거꾸로 되어있지만, 정확한 좌표를 구하는게 아닌 크기를 구하는문제
            matrix[y][x] = 1   # 그래서 굳이 좌표를 뒤집어 줄 필요없이 사각형 위치만 잘 지정해준다.

for y in range(m):
    for x in range(n):
        if matrix[y][x] == 0:
            result.append(bfs(y, x))  # 모든 matrix를 탐색하며 , 직사각형에 포함된 좌표는 1이고 포함 안된 좌표는 0  ( 좌표가 0이라면 bfs탐색 시작 )

result.sort()     # 직사각형에 포함 안된 지역들을 result에 담아 정렬 후 출력 

print(len(result))
for r in result:
    print(r, end=" ")

