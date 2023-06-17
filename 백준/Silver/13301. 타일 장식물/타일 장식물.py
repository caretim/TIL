

n= int(input())


dp = [0]*(n+1)

dp[0]=1
dp[1]=1

for i in range(2,n+1):
    dp[i]=dp[i-2]+dp[i-1]


if n == 1:
    print(4)
else:
    print(dp[n-1]*2 + (dp[n-2]+dp[n-1])*2)
#한면은 무조건 새로늘어나는 크기의 둘레,
# 나머지 면은, 현재길이+ 직전의 길이