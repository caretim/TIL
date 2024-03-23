import sys
input = sys.stdin.readline


N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(100)]for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(100):
        if L[i] <= j:
            dp[i][j] = max(J[i] + dp[i-1][j-L[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])


