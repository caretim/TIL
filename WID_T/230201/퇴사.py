n = int(input())

do = [list(map(int, input().split())) for __ in range(n)]

# print(do)

dp = [0] * (n + 1)
# print(dp)

#각 인덱스에 날짜 + 진행날자에 상담이 진행되었을때의 수익을 넣어준 후 그 날짜에 들어 갈 수 있는 수익을 넣는다.
for i in range(n):
    for j in range(i + do[i][0], n + 1):
        if dp[j] < dp[i] + do[i][1]:
            dp[j] = dp[i] + do[i][1]


print(dp[-1])
