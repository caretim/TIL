
import sys
# n= sys.stdin.readline().rstrip()

# heapq.heapify(nlist)

# for __ in range(n):
#     heapq.heappush(nlist,sys.stdin.readline().rstrip())


# print(heapq.heappop(nlist))


nls= [0]*10001
n= int(sys.stdin.readline().rstrip())
for __ in range(n):
    nls[int(sys.stdin.readline().rstrip())]+=1

for i in range(10001):
    if nls[i]>=1 :
        for __ in range(nls[i]):
            print(i)