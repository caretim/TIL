from sys import stdin
input = stdin.readline
from collections import deque

# 상이 갈 수 있는 곳
dr = (-3, -2, 2, 3, 3, 2, -2, -3)
dc = (2, 3, 3, 2, -2, -3, -3, -2)

# 위치별 장애물
obstacle = {0: ((-1, 0), (-2, 1)),
            1: ((0, 1), (-1, 2)),
            2: ((0, 1), (1, 2)),
            3: ((1, 0), (2, 1)),
            4: ((1, 0), (2, -1)),
            5: ((0, -1), (1, -2)),
            6: ((0, -1), (-1, -2)),
            7: ((-1, 0), (-2, -1))}

def bfs():
    board = [[0] * 9 for _ in range(10)]
    board[sr][sc] = 1
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()            
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            # 격자 밖으로 나가거나 이미 방문했다면
            if not (0 <= nr < 10 and 0 <= nc < 9) or board[nr][nc]:
                continue

            # 이동 중 장애물(왕) 만나면
            flag = True
            for wr, wc in obstacle[d]:
                if (r+wr, c+wc) == (kr, kc):
                    flag = False    # 그 방향으로 이동 불가 표시
                    break
            if not flag:
                continue

            if (nr, nc) == (kr, kc):    # 왕 만나면 최단 거리 리턴
                return board[r][c]
                
            # 정상 이동
            board[nr][nc] = board[r][c] + 1
            Q.append((nr, nc))
    
    return -1   # 왕에 도달하지 못하면 -1 리턴

# main
sr, sc = map(int, input().split())  # 상 위치
kr, kc = map(int, input().split())  # 왕 위치
print(bfs())