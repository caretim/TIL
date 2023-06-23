from collections import deque


n, m = map(int, input().split())
num = map(int, input().split()) 
q = deque(range(1, n+1)) 
cnt =0
for i in num:
    mid = len(q) // 2 
    if q.index(i) <= mid:  
        while q[0] != i:   
            q.append(q.popleft())
            cnt += 1
        q.popleft()
    else:                        
        while q[0] != i:
            q.appendleft(q.pop())
            cnt += 1
        q.popleft()

print(cnt)