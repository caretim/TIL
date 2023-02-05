# from collections import deque

# # 흠.. 어떻게 이동하는지 최선의 경로? 백트래킹으로 ? 찾은 후 다시 뒤로 돌아가게 for 2/1 +1 -1 로 ?
# # 진행됬던 방법을 다시 돌려서 하기 각 리스트에 넣어서 진행하긴 어렵다 근데 흠..어차피 다시 돌아서 하게되면
# # 경우의 수는 똑같을 거 같은데 .
# # bfs로 각각 진행할 때 각인덱스 숫자가 들어가는데, 이거를 어떻게 해줘여할까?? 인자를 리스트에 넣어서 진행되게???

# 1.리스트넣기 실패
# check = [0] * 100001


# n, k = map(int, input().split())

# q = deque()


# def bfs(n, k):
#     q.append((n, [n], 0))
#     check[n] = 1
#     while q:
#         x, l, cnt = q.popleft()
#         if x == k:
#             return x, l, cnt
#         for i in range(3):
#             nl = list(l)
#             if i == 0:
#                 nx = x * 2
#                 if 0 <= nx < 100001 and check[nx] == 0:
#                     check[nx] = 1
#                     nl.append(nx)
#                     q.append((nx, nl, cnt + 1))
#             elif i == 1:
#                 nx = x + 1
#                 if 0 <= (nx) < 100001 and check[nx] == 0:
#                     check[nx] = 1
#                     nl.append(nx)
#                     q.append((nx, nl, cnt + 1))
#             elif i == 2:
#                 nx = x - 1
#                 if 0 <= (nx) < 100001 and check[nx] == 0:
#                     check[nx] = 1
#                     nl.append(nx)
#                     q.append((nx, nl, cnt + 1))


# num, return_list, cnt = bfs(n, k)

# print(cnt)
# for k in return_list:
#     print(k, end=" ")


# 2. 문자열로 넣기 시간 5000ms

# import sys
# from collections import deque

# input = sys.stdin.readline
# # 흠.. 어떻게 이동하는지 최선의 경로? 백트래킹으로 ? 찾은 후 다시 뒤로 돌아가게 for 2/1 +1 -1 로 ?
# # 진행됬던 방법을 다시 돌려서 하기 각 리스트에 넣어서 진행하긴 어렵다 근데 흠..어차피 다시 돌아서 하게되면
# # 경우의 수는 똑같을 거 같은데 .
# # bfs로 각각 진행할 때 각인덱스 숫자가 들어가는데, 이거를 어떻게 해줘여할까?? 인자를 리스트에 넣어서 진행되게???


# check = [0] * 100001


# n, k = map(int, input().split())

# q = deque()


# def bfs(n, k):
#     q.append((n, str(n) + " ", 0))
#     check[n] = 1
#     while q:
#         x, l, cnt = q.popleft()
#         if x == k:
#             return x, l, cnt
#         for i in (x + 1, x - 1, x * 2):
#             if 0 <= i < 100001 and check[i] == 0:
#                 nl = l + str(i) + " "
#                 check[i] = 1
#                 q.append((i, nl, cnt + 1))


# num, return_list, cnt = bfs(n, k)

# print(cnt)
# print(return_list)
# for k in return_list:
#     print(k, end=" ")

# 3. 다른사람이 만든 이동인덱스를 재귀로 사용하여 직전의 값을 꺼내오기

# from collections import deque
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# n,k = map(int,input().split())
# MAX_INDEX = 100000
# board = [MAX_INDEX] * (MAX_INDEX+1)
# move_to = [0] * (MAX_INDEX + 1)
# q = deque()
# q.append(n)
# board[n] = 0
# while q:
#     x = q.popleft()
#     if x == k:
#         break
#     for nx in (x-1, x+1, x*2):
#         if 0 <= nx <= MAX_INDEX and board[nx] == MAX_INDEX:
#             q.append(nx)
#             board[nx] = board[x] + 1
#             move_to[nx] = x

# def move(n,m):
#     if n != m:
#         move(n,move_to[m])
#     print(m, end=' ')

# print(board[k])
# move(n,k)


import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 값이 이동할 떄 이동하기전의 값을 미리 넣어준다.

check = [0] * 100001
move = [0] * 100001


n, k = map(int, input().split())

q = deque()


def bfs(n, k):
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return
        for i in (x + 1, x - 1, x * 2):
            if 0 <= i < 100001 and check[i] == 0:
                check[i] = check[x] + 1
                move[i] = x
                q.append(i)


bfs(n, k)

print(check[k])

j = k

result_track = deque()
while n != j:
    result_track.appendleft(move[j])
    j = move[j]

result_track.append(k)

for ii in result_track:
    print(ii, end=" ")
