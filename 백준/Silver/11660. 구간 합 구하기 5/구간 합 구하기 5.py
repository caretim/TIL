import sys

input = sys.stdin.readline

# n, m = map(int, input().split())

# matrix = [list(map(int, input().split())) for __ in range(n)]


# def sum_range(x1, y1, x2, y2):
#     result = 0
#     for y in range(y1 - 1, y2):
#         for x in range(x1 - 1, x2):
#             result += matrix[y][x]
#     return result


# for case in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(sum_range(x1, y1, x2, y2))

n, m = map(int, input().split())
dp = [[0] * (n + 1) for __ in range(n + 1)]
result = []
for i in range(n):
    a = list(map(int, input().split()))
    result.append(a)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + result[i - 1][j - 1]

for k in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    r = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(r)
