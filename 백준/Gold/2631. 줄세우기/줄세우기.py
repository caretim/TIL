
import sys

n= int(input())

arr= [0]

for __ in range(n):
    arr.append(int(input()))

dp = [0]*(n+1)


for i in range(0,n+1):
    for j in range(0,i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)


print(n-max(dp))