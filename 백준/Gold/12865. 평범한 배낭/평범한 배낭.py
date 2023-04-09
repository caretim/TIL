
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0 for __ in range(100005)] for __ in range(105)]

w=[ 0 for __ in range(105)]
v=[0 for __ in range(105)]


for i in range(1, n+1):
    w[i],v[i] = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,k+1):
        if j-w[i]>=0: # 무게가 안넘을시, 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
            # dp[i-1][j]-> 직전 무게에서의 최대값, 지금 아이템의 값v[i] +  남는 무게에서의 최대값 dp[i-1][j-w[i]]
        else:
            dp[i][j]=dp[i-1][j] # 만약 무게를 초과한다면 현재무게는 전 아이템의 무게 값 ,
print(dp[n][k])