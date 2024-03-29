# n = int(input())
# cnt=0
# while n:
#     if n%3 ==0:
#         n=n//3
#     elif n-1%3 ==0:
#         n-=1
#     elif n%2==0:
#         n=n//3
#     cnt+=1

# print(cnt)

n = int(input())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:  # 2로 나누어 떨어질 때, 2로 나누는 연산
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:  # 3으로 나누어 떨어질 때, 3으로 나누는 연산 전에 있던 횟수
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])


# (x//3 , x//2 , x-1) 연산하는 최솟값2


# x = 10
# [0,0,0,0,0,0,0,0,0,0]
# 1 2 3 4 5 6   6/3 =2 , 6/2 =3 6 -1 -1 /2 /2 =4
# 0 1 1 2 3 2
