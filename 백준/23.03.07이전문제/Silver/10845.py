import sys
from collections import deque
input = sys.stdin.readline

n= int(input())
q= deque()

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
#  만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.

# top: 스택의 가장 위에 있는 정수를 출력한다.
#  만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


for __ in range(n):
    order = list(input().split())
    if order[0] == "push":
        q.append(order[1])
    elif order[0] == 'pop':
        try:
            print(q.popleft())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])

