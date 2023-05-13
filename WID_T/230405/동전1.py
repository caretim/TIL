n,k =map(int,input().split())

money=[]

for __ in range(n):
    money.append(int(input()))

dp = [0] *(k+1)
dp[0]=1

for m in money:
    for i in range(m,k+1):
        dp[i]=dp[i]+dp[i-m] #총액에 들어가는 dp[i]갱신, 

print(dp[k])