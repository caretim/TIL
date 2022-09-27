
# import sys


# n=int(input())

# nlist=[]


# for __ in range(n):
#     num= sys.stdin.readline().rstrip()
#     nlist.append(num)

# nlist.sort()

# for result in nlist:
#     print(result)




#힙정렬
import sys
import heapq
n=int(input()) # 입력 받을 원소의 갯수 

heapqlist=[] # 원소를 넣고 정열시킬 리스트 생성



for __ in range(n): # for문으로 값을 입력받고 heapqpush를 통해 값을 리스트에 넣어줌
    num= int(sys.stdin.readline().rstrip())
    heapq.heappush(heapqlist,num)
    # heapqlist.append(num)



for __ in range(n):
    print(heapq.heappop(heapqlist)) 
# 입력받은 원소의 갯수만큼 heapop을 실행하여 원소를 추출 및 프린트






