n = int(input())


dp = [0] * (301)

score = [0] * (301)


for i in range(n):
    score[i] = int(input())

# 첫번째 dp인덱스에는 무조건 첫번째 값이 들어가야하나?
dp[0] = score[0]

dp[1] = score[0] + score[1]

dp[2] = max(score[0] + score[2], score[1] + score[2])  # 점프 뛸 때 # 연달아서 올라올때


# 점프해서올때, 연달아서 계단오를때 규칙을 찾아도 점화식으로 쓰기가 너무 어려워요..

for i in range(3, n + 1):
    # dp[i]=max(dp[i-1]+dp[i],max(dp[i-2])+dp[i]) # 그래프 만들기? (점프수와 연달아오는 수 2가지의 경우의 값 구분  )
    dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])


print(dp[n - 1])
