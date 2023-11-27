import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]
dp[0] = [1] * 31
dp[0][0] = 0
for i in range(1, 31):
    for j in range(1, 31):
        if i > j:
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])