from collections import deque
import sys

input = sys.stdin.readline


n=int(input())

arr=list(map(int, input().split()))

INF= sys.maxsize

dp=[INF] *(n)


def bfs(start):
    q=deque()
    q.append((start,0))
    dp[0]=0
    while q:
        now, cnt=q.popleft()
        if arr[now]==0:
            continue
        for i in range(1, arr[now]+1):
            nxt=now+i
            if 0<=nxt<n and dp[nxt]>cnt+1:
                dp[nxt]=cnt+1
                q.append((nxt, cnt+1))
bfs(0)
if dp[n-1]==INF:
    dp[n-1]=-1
print(dp[n-1])