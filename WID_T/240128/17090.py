# import sys
# from collections import deque

# input =sys.stdin.readline


# n,m= map(int,input().split())

# dict={
#     'U':[-1,0],
#     'R':[0,1],
#     'D':[1,0],
#     'L':[0,-1]
# }

# matrix= [list(input()) for __ in range(n)]

# dp = [[0]*(m) for __ in range(n)]


# def bfs(y,x):
#     q=deque()
#     q.append((y,x,[(y,x)]))
#     visited = [[0]*(m) for __ in range(n)]
#     visited[y][x]= 1
#     while q:
#         y,x,move = q.pop()
#         if dp[y][x] == 0:
#             ny,nx = y+dict[matrix[y][x]][0], x+dict[matrix[y][x]][1]
#             if 0<=ny<n and 0<=nx<m:
#                 if visited[ny][nx]==0:
#                     visited[ny][nx] = 1 
#                     new_move = move
#                     new_move.append((ny,nx))
#                     q.appendleft((ny,nx,new_move))
#             else:
#                 for ny,nx in move:
#                     dp[ny][nx] = 1
#                 return
            
#         elif dp[y][x] == 1: # 이미 갔던길이고 탈출에 성공한 길이라면 
#             for ny,nx in move:
#                 dp[ny][nx] = 1
#             return 

#     for y in range(n): # 모든 경우를 돌고 탈출 못했다면 방문했던 리스트 모두 -1(실패처리)
#         for x in range(m):
#             if visited[ny][nx] == 1:
#                 dp[ny][nx] = -1
#     return

        
    

# for y in range(n):
#     for x in range(m):
#         if dp[y][x] == 0:
#             bfs(y,x)

# cnt =0
# for y in range(n):
#     for x in range(m):
#         if dp[y][x] ==1:
#             cnt+=1


# print(cnt)


# for문 많아서 시간초과

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input().rstrip())

visited = [[0 for i in range(M)]for j in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        Q = deque()
        path = set()
        Q.append((i, j))
        path.add((i, j))
        while Q:
            cx, cy = Q.popleft()
            cmd = board[cx][cy]
            if cmd == "U":
                cx -= 1
            elif cmd == "D":
                cx += 1
            elif cmd == "L":
                cy -= 1
            elif cmd == "R":
                cy += 1
            if cx < 0 or cx >= N or cy < 0 or cy >= M or visited[cx][cy] == 2:
                for px, py in path:
                    visited[px][py] = 2
                    ans += 1
                break
            if (cx, cy) in path or visited[cx][cy] == 1:
                for px, py in path:
                    visited[px][py] = 1
                break
            path.add((cx, cy))
            Q.append((cx, cy))
print(ans)
