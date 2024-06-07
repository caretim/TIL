import sys

input = sys.stdin.readline


for __ in range(int(input())):
    n= int(input())

    coin = list(map(int,input().split()))

    m=int(input())
    dp = [0] *(m+1)
    dp[0] = 1

    for i in range(n):
        for j in range(coin[i], m+1):
            dp[j] += dp[j-coin[i]]

    print(dp[m])