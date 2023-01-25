# n, m = map(int, input().split())


# board = [[0] for __ in range(101)]

# good = []

# bad = []

# count = 0


# for __ in range(n):
#     x, y = map(int, input().split())
#     board[x] = y
#     if y - x > 6:
#         good.append(x)

# for __ in range(m):
#     x, y = map(int, input().split())
#     board[x] = y
#         bad.append(x)


# def throw(a):
#     global count
#     count += 1
#     for i in range(6, 0, -1):
#         if a + i == 100:
#             return
#         elif a + i in good:
#             count += 1
#             throw(board[a + i])
#             return
#         elif a + i in bad:
#             pass
#         else:
#             count += 1
#             throw(a + i)
#             return


# throw(1)

# print(count)
from collections  import deque

dice = [1,2,3,4,5,6]

n, m = map(int, input().split())


board = [0]*101
check = [0]*101

good = []

bad = []


for __ in range(n):
    x, y = map(int, input().split())
    board[x] = y
    check[x] = -2
    if y-x > 6:
        good.append((x,y))

for __ in range(m):
    x, y = map(int, input().split())
    board[x] = y
    check[x] = -2
    bad.append((x,y))


def bfs(x):
    q = deque()
    check[x] = 'start'
    q.append((x,0))
    while q:
       x,y= q.popleft()
       for i in range(6):
        nx =x+dice[i]
        if nx < 101:
            if check[nx]==0:
                check[nx]=y+1
                q.append((nx,y+1))
            if check[nx]==-2:
                check[nx]=y+1
                q.append((board[nx],y+1))




        
bfs(1)
print(check[100])



# 뱀을 피해서 사다리를 타고 올라가야함 사다리가 6칸 이상의 이동을 보장 할 떄 사다리 사용 외에는 주사위와 같다
