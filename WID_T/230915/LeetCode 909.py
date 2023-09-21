import heapq
import sys

INF = sys.maxsize
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1 ,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[ -1,15,-1,-1,-1,-1]]
n= len(board)
line = [-1]
flag = 1
for y in range(n-1,-1,-1):
    if flag%2 ==1:
        for x in range(n):
            line.append(board[y][x])
    else:
        for x in range(n-1,-1,-1):
            line.append(board[y][x])
    flag+=1

visit = [INF] *((n**2)+1)
visit[1]=0
q= []
heapq.heappush(q,(0,1))
while q:
    move,cur = heapq.heappop(q)
    for i in (1,2,3,4,5,6):
        next = cur+i
        if line[next]!= -1:
            next = line[next]
        if next <(n**2) and visit[next]>move+1:
            visit[next]=move+1
            heapq.heappush(q,(move+1,next))
            # print(move,next)
        if next == (n**2):
            print(move+1)
            exit()


# from collections import deque

# class Solution(object):
#     def snakesAndLadders(board):
#         n= len(board)
#         line = [-1]
#         flag = 1
#         for y in range(n-1,-1,-1):
#             if flag%2 ==1:
#                 for x in range(n):
#                     line.append(board[y][x])
#             else:
#                 for x in range(n-1,-1,-1):
#                     line.append(board[y][x])
#             flag+=1
#         print(line)
#         visit =[0]*((n**2)+1)
#         visit[1]=1
#         q= deque()
#         q.append((0,1))
#         while q:
#             move,cur = q.popleft()
#             for i in (1,2,3,4,5,6):
#                 next = cur+i
#                 if line[next]!=-1:
#                     next = line[next]
#                 if visit[next] ==0:
#                     visit[next] = move+1
#                     q.append((move+1,next))
#                     print(next)
#                 if n**2 == next:
#                     return move+1

#         return -1


    
# board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

# print(Solution.snakesAndLadders(board))