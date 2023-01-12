# 1일때 1 , 2일때 2 3일때 3 4일때 5 피보나치수열문제랑 앞의 인덱수 두개를 더한값


n = int(input())

dp = [0] * (n + 1)

# if n <= 1:
#     dp[1] = 1
#     print(dp[n])
# elif n <= 2:
#     dp[2] = 2
#     print(dp[n])
# else:
dp[1] = 1
dp[2] = 2


for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    if i == n:
        print(dp[n] % 10007)
