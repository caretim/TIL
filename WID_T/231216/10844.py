import sys

input = sys.stdin.readline

n = int(input())

# dp = [[0] * 10 for _ in range(n+1)]


# dp[0] = 0

# dp[1] = 9
# dp[2] = 17
# print(dp)


dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]  # 0일때  01만 가능

        elif 1 <= j <= 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

        elif j == 9:  # 9일떄  98 만 가능
            dp[i][j] = dp[i - 1][8]

print(sum(dp[n]) % 1000000000)