import sys
input = sys.stdin.readline

x,y = map(int, input().split())

matrix = [[0 for i in range(y+1)] for _ in range(x+1)]

dp = [[0 for i in range(y+1)] for _ in range(x+1)]

for i in range(1,x+1):
    tmp = list(map(int, input().split()))
    tmp.insert(0,0)
    matrix[i] = tmp

for i in range(1,x+1):
    for j in range(1,y+1):
        dp[i][j] = max(matrix[i][j] + dp[i][j-1], matrix[i][j] + dp[i-1][j])

print(dp[x][y])