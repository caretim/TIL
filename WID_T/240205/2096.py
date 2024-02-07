# import sys
# input =sys.stdin.readline

# inf  =sys.maxsize

# n= int(input())


# matrix = [list(map(int,input().split())) for __ in range(n)]



# dp = [[[0,0],[0,0],[0,0]] for __ in range(n)]

# print(matrix)

# #0과 n일때 2칸씩만 체크
# # for문 진행하면서 최소값 최대값 dp로 저장

# for i in range(3):
#     dp[0][i][0] = matrix[0][i]
#     dp[0][i][1] = matrix[0][i]

# print(dp)

# for y in range(1,n):
#     for x in range(3):
#         if x == 0:
#             dp[y][x] = max(dp[y-1][x][0],dp[y-1][x+1][0])+ matrix[y][x] 

        #     dp[y][x] = min(dp[y-1][x][1],dp[y-1][x+1][1])+ matrix[y][x] 
        # elif x == 2:
        #     dp[y][x] = max(dp[y-1][x][0],dp[y-1][x-1][0])+ matrix[y][x] 
        #     dp[y][x] = min(dp[y-1][x][1],dp[y-1][x-1][1])+ matrix[y][x] 
        # else:
        #     dp[y][x] = max(dp[y-1][x][0],dp[y-1][x-1][0],dp[y-1][x+1][0])+ matrix[y][x] 
        #     dp[y][x] = min(dp[y-1][x][1],dp[y-1][x-1][1],dp[y-1][x+1][1])+ matrix[y][x] 
                



# print(max(dp[n-1]),min(dp[n-1]))
import sys
input =sys.stdin.readline
n = int(input().rstrip())
maxdp = [0, 0, 0]
mindp = [0, 0, 0]
maxdp[0], maxdp[1], maxdp[2] = map(int, input().rstrip().split())
mindp[0], mindp[1], mindp[2] = maxdp[0], maxdp[1], maxdp[2]


for i in range(1, n):
    num0, num1, num2 = map(int, input().rstrip().split())
    maxdp = [max(maxdp[0], maxdp[1]) + num0, max(maxdp[0], maxdp[1], maxdp[2]) + num1, max(maxdp[1], maxdp[2]) + num2]
    mindp = [min(mindp[0], mindp[1]) + num0, min(mindp[0], mindp[1], mindp[2]) + num1, min(mindp[1], mindp[2]) + num2]

print(max(maxdp), min(mindp))


