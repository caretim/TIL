import sys

sys.setrecursionlimit(10**7)

n = int(input())

dp = [0] * 320


cnt = 0


def divide(k):
    if k == 0:
        return
    global cnt
    for i in range(len(dp)):
        if dp[i] > k:
            k = k - dp[i - 1]
            cnt += 1
            divide(k)
            # print(i, "제곱수")
            # print(k, "나머지값")
            break


for i in range(len(dp)):
    dp[i] = i * i
    if dp[i] > n:
        k = n - dp[i - 1]
        cnt += 1
        divide(k)
        # print(i)
        # print(k)
        break

print(cnt)
