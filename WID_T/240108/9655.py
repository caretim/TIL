n = int(input())

dp = [0] * (n + 1)


dp[1] = 1
dp[2] = 2
dp[3] = 1
dp[4] = 2

for i in range(5, n + 1):
    if dp[i - 1] == 1 or dp[i - 3] == 1:
        dp[i] = 2
    else:
        dp[i] = 1


print(dp)
if dp[n] == 1:
    print("SK")
else:
    print("CY")
