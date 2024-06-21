from collections import deque
n,k= map(int,input().split())


result = deque()
que = deque()
next_que=deque()


for i in range(n):
    que.append(i+1)


cnt = 0
while que:
    for i in que:
        cnt+=1
        if cnt % k ==0:
            result.append(i)
        else:
            next_que.append(i)
    que = next_que
    next_que = deque()

print('<',end='')
print(*result,sep=', ',end='')
print('>')
