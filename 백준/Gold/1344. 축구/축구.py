import sys

input = sys.stdin.readline

# 5분 간격  90분 총 18개의 구간 존재
# 각 팀의 골은 독립적으로 시행된다

# 마지막 구간에서 두팀 중 소수 - 2,3,5,7,9,11,13,17 중 (최대 18골 가능)의 점수로 게임마감하는경우

# 각팀의 dp로 확인 
dp = [[[0 for _ in range(19)] for _ in range(2)] for _ in range(18)]



a = int(input())/100
b = int(input())/100


dp[0][0][0], dp[0][0][1] = 1-a, a # a팀 

dp[0][1][0], dp[0][1][1] = 1-b, b # b팀

# 경기 구간마다 득점 확률 계산  현재 구간에서 -1 점수 구간 * 현재 팀 득점확률  
for i in range(1, 18):
    for j in range(2):
        if j == 0:
            for k in range(19):
                dp[i][j][k] = dp[i-1][j][k-1]*a + dp[i-1][j][k]*(1-a)
        else:
            for k in range(19):
                dp[i][j][k] = dp[i-1][j][k-1]*b + dp[i-1][j][k]*(1-b)

nums = [2, 3, 5, 7, 11, 13, 17]


a_socre = 0
b_score = 0
for num in nums:
    a_socre += dp[17][0][num]
    b_score += dp[17][1][num]

print(1 - (1-a_socre)*(1-b_score))
