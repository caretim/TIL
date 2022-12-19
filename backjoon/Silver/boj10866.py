# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys


deq = deque([])


n = int(input())

for __ in range(n):
    input_list = list(sys.stdin.readline().split())
    if input_list[0] == "push_front":
        deq.appendleft(input_list[1])
    elif input_list[0] == "push_back":
        deq.append(input_list[1])
    elif input_list[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif input_list[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif input_list[0] == "size":
        print(len(deq))
    elif input_list[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif input_list[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif input_list[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
