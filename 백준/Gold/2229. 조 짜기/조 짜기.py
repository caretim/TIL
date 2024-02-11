n = int(input())

# 나이 순서대로 정렬되어있음
score = list(map(int,input().split()))



# 나이 차 

dp = [0]*n
for i in range(n) :
  min_s = max_s = score[i]
  for j in range(i+1, n) :
    min_s = min(min_s, score[j])
    max_s = max(max_s, score[j])
    now = dp[i-1] if i > 0 else 0
    dp[j] = max(dp[j], max_s - min_s + now)

print(dp[-1])