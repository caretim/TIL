# N= int(input())

# A,B= map(int,input().split())
# C = int(input())

# D = []

# for __ in range(N):
#     D.append(int(input()))

# sorted(D, reverse=True)

# cnt=0

# L  =C//A

# n= 0

# for i in D:
#     cnt+=i
#     n+=1    
#     money = (C+cnt) // (A+B*N)
#     if money>=L:
#         L=money

# print(L)




N = int(input())
A, B = map(int, input().split())
C = int(input())
lst, res = [], 0
for _ in range(N):
    lst.append(int(input()))
 
lst = sorted(lst, reverse=True)
for i in range(len(lst)+1):
    price = A + B * i
    res = max(res, (C+sum(lst[:i]))//price)
print(res)