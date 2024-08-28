import sys,heapq


input = sys.stdin.readline


n,l = map(int,input().split())

nums =  list(map(int,input().split()))

#값을 뽑는건 최소힙을 통해서 제일 낮은 값 빼기
# 인덱스에 따라 힙이 구성되어야하는데 인덱스 순서의 번호로 값을 어떻게뺴주지?
# 튜플의 형태로 인덱스 순서, 값을 넣는다고하면? 람다함수로 계산해주면 되지만
# 내부의 튜플 값을 기준으로 최소힙을 x  -> heapq.push로 저장하면 값이 맨 앞의 값을 기준으로 
heap = []
lCnt= -l
result = []
for i in range(n):
    lCnt+=1
    heapq.heappush(heap,(nums[i],i))
    while lCnt>heap[0][1]:
        heapq.heappop(heap)
    result.append(heap[0][0])
print(*result)
# class numa:
#     def __init__(a,b):
#         numa.index = a
#         numa.val = b

# for i in range(l):
#     if minResult>nums[i]:
#         minResult = nums[i]
#         heapq.heappush(temp,(i,nums[0]))
#     print(minResult)

# heapq.heappush(temp,(0,nums[0]))
# for i in range(l,n):
#     if minResult>nums[i]:
#         minResult = nums[i]
#     heapq.heappush(temp,(i,nums[0]))
#     ex = heapq.heappop(temp)
#     if ex == 
#     print(minResult)

    

