# n = int(input())
n = 0
dp = [0] * (n + 1)
if n == 0:
    print(0)
    exit()
dp[1] = 1


for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]


print(dp[n])
