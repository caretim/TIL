import sys


n, m = map(int, input().split())


nlist = list(map(int, input().split()))

sum_list = [0]

suml = 0

for sn in nlist:
    suml += sn
    sum_list.append(suml)


for __ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    result = sum_list[y] - sum_list[x - 1]
    print(result)

# for __ in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     nsum = 0
#     x -= 1
#     for idx in range(x, y):
#         nsum += nlist[idx]

#     print(nsum)

# 시간초과
# for __ in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     nsum = 0
#     x -= 1
#     for idx in range(x, y):
#         nsum += nlist[idx]

#     print(nsum)
