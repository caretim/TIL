n = int(input())
blocks = list(input())
pre = {'B': 'J', 'O': 'B', 'J': 'O'}
dp = [0] + [10000001]*n 

for i in range(1, n): 
    p = pre[blocks[i]] 
    for j in range(i): 
        if blocks[j] == p:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

if dp[n-1] == 10000001:
    print(-1)
else:
    print(dp[n-1])