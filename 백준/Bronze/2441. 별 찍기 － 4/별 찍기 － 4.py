from collections import deque

n = int(input())

start=[]

# for __ in range(n):
#     start.append('*')

# print(*start)

# for i in range(n-1):
#     start[i]=' '
#     print(*start)
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*(i))    
