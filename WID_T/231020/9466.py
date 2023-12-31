import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# for __ in range(int(input())):
#     n = int(input())

#     def list_num(l):
#         nums = []
#         for i in l:
#             nums.append(i - 1)
#         return nums

#     list_input = list(map(int, input().split()))

#     students = list_num(list_input)

#     dict = {}

#     for i in range(n + 1):
#         dict[i] = [-1, -1]  # 현재팀,자신의 순서

#     def dfs(now, next, cur):
#         if now == next:
#             dict[now] = [-(now + 10), 0]
#             return
#         team = []
#         stack = []
#         stack.append(next)
#         team.append(now)
#         cnt = 0
#         dict[now] = [cur, cnt]
#         while stack:
#             cnt += 1
#             now = stack.pop()
#             next = students[now]
#             if now == next:
#                 dict[now] = [-(now + 10), 0]
#                 return team
#             if dict[next][0] == -1:  # 아무팀에 소속되어있지않을 경우
#                 team.append(now)
#                 stack.append(next)
#                 dict[now] = [cur, cnt]
#             elif dict[next][0] == cur:  # 같은 팀일 경우,
#                 team.append(now)
#                 if dict[next][1] == 0:
#                     dict[now] = [cur, cnt]
#                     return team[: dict[next][1]]
#         return team

#     result = 0
#     cur = 0
#     for i in range(len(students)):
#         if dict[i][0] == -1:
#             t = dfs(i, students[i], cur)

#             if t:
#                 result += len(t)
#             cur += 1

#     print(result)


def dfs(x):
    global ans
    vis[x] = True
    cycle.append(x)
    num = arr[x]

    if vis[num]:
        if num in cycle:
            ans += cycle[cycle.index(num) :]
        return
    else:
        dfs(num)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    vis = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not vis[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))
