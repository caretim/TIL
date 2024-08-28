import sys,heapq

input =sys.stdin.readline


n,d = map(int,input().split())


brg = list(map(int,input().split()))

#d의 값만큼의 길이의 우선순위큐를 가지고 각 인덱스 방문후 값 갱신하기, 가장 큰수를 갱신?
# heap에 d의 범위로 나올 수 있는 값을 갱신하기 ,
# 각 값을 
# heapq pop을 통해서 인덱스의 d값보다 크다면 pop을 통해 현재값 뺴기 ,

dp = [0] * (n+1)

#d값 만큼 값 갱신해서 각 값 넣어주기 ? - > n의 범위가 너무 넓음 ,
# 숫자가 더해질떄 갱신될 수 있는 유효한 값인지 알아야함 
# 범위 이내의 값중 최대로 갱신 될 수 있는 값 - > pop으로 뽑지말고 음수처리 후 0번쨰 인덱스로 확인 
# d의범위 이내 
# dp[0] = brg[0]
# dp[1] = max(dp[0],dp[0]+brg[1])
# dp[2] = brg[2]
#->> d 가 2 일 경우 
# for i in range(3,len(brg)):
#     dp[i] = max(brg[i],brg[i-1]+brg[i],brg[i-2]+brg[i])
#     result =max(dp[i],result)

heap = []

result = brg[0]
# heapq.heappush(heap,(-dp[0],0))
for i in range(n):
    dp[i] = brg[i]
    #D값을 벗어나는 값 heap에서 지워주기 ,
    while heap and i-heap[0][1]>d:
        heapq.heappop(heap)
    if heap:
        dp[i] = max(dp[i],dp[i]-heap[0][0])
        result = max(result,dp[i])

    heapq.heappush(heap,(-dp[i],i))

print(result)




 