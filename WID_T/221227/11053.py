from collections import deque

n = int(input())

num_list = list(input().split())

result=[]

dp = [0 for__ in range(n)]

for num in num_list:
    



print(len(result))

# q = deque()


# for num in num_list:
#     if len(q) == 0:
#         q.append(num)
#     elif len(q) == 1:
#         if q[0] < num:
#             q.appendleft(num)
#         elif q[0] > num:
#             q.pop()
#             q.appendleft(num)
#     elif q[0] > num and q[1] < num:
#         q.pop()
#         q.appendleft(num)
#     elif q[0] < num:
#         q.appendleft(num)
# q.reverse()

# print(len(q))

