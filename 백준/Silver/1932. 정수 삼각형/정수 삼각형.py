import sys

input = sys.stdin.readline

n = int(input())

num_list = [list(map(int, input().split())) for __ in range(n)]

dp = [[] for __ in range(len(num_list))]

dp[0].append(num_list[0][0])


for j in range(1, len(num_list)):  # 맨 첫줄 시작을 어떻게?
    for i in range(len(num_list[j])):
        if i == 0:
            dp[j].append(dp[j - 1][i] + num_list[j][i])
        else:
            try:  # 첫번아닐때
                dp[j].append(
                    max(
                        dp[j - 1][i - 1] + num_list[j][i], dp[j - 1][i] + num_list[j][i]
                    )
                )
            except:  # 인덱스 오류나서 자기가 막번일떄
                dp[j].append(dp[j - 1][i - 1] + num_list[j][i])


print(max(dp[n - 1]))
