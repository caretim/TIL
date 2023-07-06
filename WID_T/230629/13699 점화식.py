n= int(input())

dp = [0 for __ in range(n+1)]

dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=5
#t(n-1)*t(0)
# t(1)=t(0)*t(0)=1
# t(2)=t(0)*t(1)+t(1)*t(0)=2
# t(3)=t(0)*t(2)+t(1)*t(1)+t(2)*t(0)=5

if n>3:

    for i in range(4,n+1):
        for j in range(i):
            dp[i]+= dp[j]*dp[i-j-1]

print(dp[n])
     
