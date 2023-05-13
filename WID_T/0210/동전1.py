# n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

# 사용한 동전의 구성이 같은데, *** 중요 순서만 다른 것은 같은 경우이다.


# 순서만 다른 것은 같은 경우 ,  -> k직전에 경우의수의 최대값 훔,,  시간 0.5초 4mb면 그냥 n으로 쭉 가서 한번에 끝내기

# 1*5 1*3,2*1 1*1,2*2 
 # dp에 각 경우의 수를 더해주고 각 디피는 
n, k = map(int, input().split())

dp = []

for _ in range(n):
    dp.append(int(input()))
    
dp[0] = 1

dp = [0] * (k+1)

for coin in dp:
    for i in range(coin, k+1):
        coins = dp[i - coin]
        dp[i] += coins
print(dp[k])