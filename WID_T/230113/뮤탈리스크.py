# 한 번의 공격에서 같은 SCV를 여러 번 공격할 수는 없다.

# 9 3 1
# 최대힙으로 가장 큰 수 중간수 계속 정렬시키면서 값 빼주기?

# 최대힙 또는 람다함수로 값 계속 정렬시켜주며 9,3,1씩 뺴주기,

import heapq
from collections import deque
import pprint

n = int(input())

scv = list(map(int, input().split()))

# 각 리스트를 탐색하면서 방문리스트에 값,횟수 적어주기 , 범위는 60*60*60 탐색하면서 0,0,0에 도달시 멈춤
# 6개의 경우의수를 대입하며 bfs탐색 숨바꼭질이라면? 어떻게?
count = 0
damage = [
    (-9, -3, -1),
    (-9, -1, -3),
    (-1, -9, -3),
    (-3, -9, -1),
    (-1, -3, -9),
    (-3, -1, -9),
]  # 6가지 bfs탐색

check = [[[0] * 61 for __ in range(61)] for __ in range(61)]

len(check)

while len(scv) < 3:
    scv.append(0)

# for i in check:
#     # for j in i:
#     print(i)


def bfs(x, y, z):
    attack = deque()
    attack.append((x, y, z, 0))
    check[x][y][z] = 1
    while attack:  # 만약 hp가 음수로 넘어가게되면 ??? 그냥 0으로 치환해서 넣어주면될듯??? 굳이 계산더안해줘도됨
        x, y, z, a = attack.popleft()
        for i in range(6):
            ax, ay, az = damage[i]
            nx = ax + x
            ny = ay + y
            nz = az + z
            if nx < 0:
                nx = 0
            if ny < 0:
                ny = 0
            if nz < 0:
                nz = 0
            if (nx, ny, nz) == (0, 0, 0):
                print(a + 1)
                exit()
            elif check[nx][ny][nz] == 0:
                check[nx][ny][nz] = 1
                attack.append((nx, ny, nz, a + 1))
                print(nx, ny, nz, a + 1)


bfs(scv[0], scv[1], scv[2])
# # scv가 3마리가 아니라면 ? 순서에따라 카운트 돌아가면서
# while True:
#     scv.sort(reverse=True)
#     print(scv)
#     if scv[0] <= 0:
#         break
#     for i in range(n):
#         scv[i] -= damage[i]
#     count += 1
# print(count)
