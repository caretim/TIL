
# 1,2,3,4,5,6,7,8,9

# 10,12,21,23,34,34,45,56,67,78,89,21,32,34,45,56,67,78,89

# 0 으로 시작 할 때는 포함 안됨 
n=int(input())

dp = [[0] * 10 for _ in range(n + 1)]


for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1): 
    for j in range(10):
        if j ==0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else: 
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[n]) % 1000000000)