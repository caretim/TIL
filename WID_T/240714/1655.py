import sys

import heapq

input = sys.stdin.readline



n= int(input())


top_heap = []
bottom_heap =[]

for i in range(n):
    num= int(input())
    if len(bottom_heap) ==0 or  -bottom_heap[0]>= num:
        heapq.heappush(bottom_heap,-num)
    else:
        heapq.heappush(top_heap,num)


    if len(bottom_heap)>len(top_heap)+1:
        j = heapq.heappop(bottom_heap)
        heapq.heappush(top_heap,j) 

    elif len(top_heap)>len(bottom_heap):
        k = heapq.heappop(top_heap)
        heapq.heappush(bottom_heap,-k) 

    print(-bottom_heap[0])



#최소힙과 최대힙, 두개 사용 , 왜 ? 두가지를 사용할까? 

# heap은 0번쨰 인덱스에 가장 작은 값을 보관함, 

# 만약 pop을 한다면 각 원소가 두번씩 줄어들어서 동일한 원소가 나오는 순간이 중간값?

# 2개의 원소가 중앙값이라면 순서가 거꾸로 나와있음, 그냥 삽입된 순서 나누기//2하는게 제일 빠름,

# 위의 방법으로 시행한다면 단순히 pop연산속도가 2배 빨라짐,
