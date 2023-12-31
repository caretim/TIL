# import sys

# from collections import deque

# input = sys.stdin.readline

# # 각각 도착지점 확인,
# dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]  # =상,하, 좌, 우

# dict = {
#     0: [(-3, -2), (-2, -1)],
#     1: [(-2, 1), (-3, 2)],
#     2: [(2, -1), (3, -2)],
#     3: [(2, 1), (3, 2)],
#     4: [(1, -2), (2, -3)],
#     5: [(-1, -2), (-2, -3)],
#     6: [(-1, 2), (-2, 3)],
#     7: [(1, 2), (2, 3)],
# }


# print(dict[0][0][0])
# print(dict[0][0][1])
# INF = sys.maxsize

# matrix = [[-1] * 9 for __ in range(10)]


# def game(sy, sx, ky, kx):
#     q = deque()
#     matrix[sy][sx] = 0
#     q.append((sy, sx, 0))
#     while q:
#         y, x, cnt = q.pop()
#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]
#             if 0 <= ny < 9 and 0 <= nx < 10 and matrix[ny][nx] == -1:
#                 flag = 1
#                 for ii in range(2):
#                     for iii in range(2):
#                         iy, ix = (
#                             y + dict[(i % 2) + ii][iii][0],
#                             x + dict[(i % 2) + ii][iii][1],
#                         )
#                         if iii == 0 and matrix[iy][ix] == 1:
#                             break
#                         else:
#                             matrix[iy][ix] = 1
#                             if (ky, kx) == (iy, ix):
#                                 return cnt + 1
#                             q.appendleft((iy, ix, cnt + 1))


# sy, sx = map(int, input().split())
# ky, kx = map(int, input().split())


# game(sy, sx, ky, kx)
# print(matrix)
