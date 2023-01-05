from collections import deque

n, m = map(int(input().split()))

check =[0]*(m+1)

dp = [0]*(m+1)




#점화식 = x-1, x+1 x*2


def find(n,m):
    q= deque([n,0])
    while q:
        v,j = q.popleft()
        if v==m:
            return(v)
        for k in (v-1,v+1,v*2):
            k.append()




find(n,m)

