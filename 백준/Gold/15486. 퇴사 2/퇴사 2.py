import sys
input =sys.stdin.readline

n= int(input())

T=[]
P =[]

dp =[0]*(n+1)

for __ in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)


for i in range(n):
    dp[i] =max(dp[i-1],dp[i]) #현재 날짜에서 최대 값
    if i+T[i]<n+1:
        dp[i+T[i]]= max(dp[i]+P[i],dp[i+T[i]])
print(max(dp))