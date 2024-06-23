import sys

input =sys.stdin.readline


n = int(input())

k = int(input())

import heapq
senser = list(map(int,input().split()))


senser.sort()

#구간에서의 길이 연달아 나오는 구간합  , 
# - 직전의 숫자보다 수가 커진다면 따로 분리
# - 구간별 직전 구간과 절대값 차이 구하기 ,

# k= 1, 2, 3 일떄
# 1 3 6 7 9
# 절대값 범위 2,3,1,2,
#k= 5
# 3, 6, 7, 8, 10, 12, 14, 15, 18, 20
#   3, 1, 1, 2, 2,  2,   1,  3  2 

# 각수의 절대값 힙으로 넣고 뺀 뒤 수 계산 , 만일 1이라면 가장 적은수에서 가장 큰수까지 
result = 0
if n>=k:
    abs_num = []
    now= senser[0]
    for i in range(1,len(senser)):
        heapq.heappush(abs_num,(-abs(now-senser[i])))
        now =senser[i]
    for __ in range(k-1):
        heapq.heappop(abs_num)
    result = -sum(abs_num)
    
    
print(result)