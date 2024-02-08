import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())
dp = [[0] * i for i in range(50)]
for i in range(1, 30):
    for j in range(i):
        if j == 0 or j == i - 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

ans = 0
for i in range(w):
    for j in range(i+1):
        ans += dp[i+r][j+c-1]
print(ans)