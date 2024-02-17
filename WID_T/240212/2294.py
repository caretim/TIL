from collections import deque
import sys
input= sys.stdin.readline


n,k= map(int,input().split())

inf= sys.maxsize

coin = []

for __ in range(n):
    coin.append(int(input()))


dp =[inf]*(k+1)
dp[0] =0
q=deque()

q.append((0,0))
while q:
    now,cnt = q.pop()
    if dp[now]>cnt:
        continue
    for i in coin:
        if  now+i<k+1 and cnt+1 < dp[now+i]:
            dp[now+i] =cnt+1
            q.appendleft((now+i,cnt+1))

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])



