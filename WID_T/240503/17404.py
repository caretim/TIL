import sys
input =sys.stdin.readline

INF = 400000000
n= int(input())

color_values = [list(map(int,input().split())) for __ in range(n)]


#시작과 끝은 색이 달라야한다.
#각 노드의 인접노드와 색이 달라야한다.

# 시작점과 끝점 값 비교해서 시작값 끝값 절대값으로 결정
# 중간노드 선택 분기 나눠서 가기?
# last_n = {1:[0,2], 2:[1,0],0:[1,2]}

result=INF
for i in range(3):
    dp = [[INF,INF,INF] for __ in range(n)]
    dp[0][i] = color_values[0][i]
    for j in range(1,n):
        dp[j][0] = min(dp[j-1][1],dp[j-1][2]) +color_values[j][0]
        dp[j][1] = min(dp[j-1][0],dp[j-1][2]) +color_values[j][1]
        dp[j][2] = min(dp[j-1][1],dp[j-1][0]) +color_values[j][2]
    dp[j][i] =INF
    curMin  = min(dp[n-1])
    result = min(result,curMin)
print(result)

