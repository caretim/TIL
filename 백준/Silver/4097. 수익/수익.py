import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n==0:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    dp = [0 for _ in range(n)]
    
    dp[0] = arr[0]
    
    for i in range(1,n):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    print(max(dp))