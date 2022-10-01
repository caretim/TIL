import sys


n, m = map(int, input().split())


nlist = list(map(int, input().split()))

sum_list = [0]  # 인덱스 범위 설정을 위해서 기본 인덱스에 0을 넣어줌 (범위 벗어남 방지와 숫자를 바로 대입하기위해)

suml = 0

for sn in nlist:  # 각 인덱스 구간이 늘어날 때 마다 리스트 인덱스에 값을 보관한다.
    suml += sn
    sum_list.append(suml)


for __ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    result = (
        sum_list[y] - sum_list[x - 1]
    )  # 찾으려는 인덱스의 구간 합을 미리 sum_list에 넣어놨기에 찾으려는 구간의 마지막 인덱스와
    print(result)  # 첫 인덱스를 sum_list인덱스에서 찾아온다  첫인덱스에서 -1을 하게되면 x부터 y의 인덱스 합의 값이 남게된다.

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
