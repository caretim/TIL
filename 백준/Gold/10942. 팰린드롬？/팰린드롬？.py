import sys

input = sys.stdin.readline

def palindrome(s,e):
    pass

n = int(input())
arr= list(map(int,input().split()))

m =int(input())

dp = [[False]*(n) for __ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i < n-1:
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 1

for j in range(2,n):
    for i in range(n-j):
        if arr[i]==arr[i+j] and dp[i+1][i+j-1]==1:
            dp[i][i+j]=1



for __ in range(m):
    s,e = map(int,input().split())
    if dp[s-1][e-1]:
        print(1)
    else:
        print(0)

# for d in dp:
#     print(d)