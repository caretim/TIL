n, m = map(int, input().split())


# 1 1 1 1 1 1 1 1
# 2 3 4 5 6 7 8 9
# 3 6 10 15 21 29 37 36

# dp [m][n] =dp[m][n-1] + dp[m-1][n] 대각선으로 더해주면 좌표값나옴

INF = 10**9

dp = [[0] * (201) for __ in range(201)]

for j in range(1, 201):
    dp[1][j] = 1

for y in range(2, 201):
    for x in range(1, 201):
        dp[y][x] = dp[y][x - 1] + dp[y - 1][x]


print()
