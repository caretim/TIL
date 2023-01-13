# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
#  이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는
#   현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
import pprint
import sys

input = sys.stdin.readline

n = int(input())

num_list = [list(map(int, input().split())) for __ in range(n)]

dp = [[] for __ in range(len(num_list))]

dp[0].append(num_list[0][0])

print(dp)
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

# 최대값,  7 + 3 , 7+8 ,

# 본인의 인덱스 또는 본인의 인덱스 -1  범위를 벗어날때는 예외처리

# 맨 마지막 줄만 그래프탐색 진행 n-1번째 인덱스부터 시작해서 0번쨰 리스트번호까지 올라가기 ,
# 경우가 여러가지인데 흠 , ,어차피 커지려고하면 위에서 내려오면서
# 삼각형리스트를 만들어서 각 위치마다 위에서 내려올떄 가장 큰 값일 경우 ?
#
# 2번리스트 최고값   [18][16][15]
# 3번리스트 최고값 [20][23][20][19]
# 위에서 인접해서 내려오는 리스트의 값 + 본인의 인덱스 값 인덱스 처음과 마지막 제외
# 제외된 값들은 전 인덱스의 점화식 =  dp [i -1]과 dp[i] 중 max값 + 본인 값
# dp[i]= max(dp[j-1][i-1]+num_list[i],dp[j-1][i-1]+num_list[i]
# 예외처리는 처음과 마지막인덱스는 따로 처리, try문으로?

# 합을 마지막줄 인덱스 번호만큼
