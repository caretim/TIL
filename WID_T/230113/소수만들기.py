from itertools import combinations
#에라토스테네스의 체 구현
max_num = 3000

num = [0]*3001

m = int(max_num**0.5)

for i in range(2,m):
    if num[i] == 0:
        for j in range(i+i,max_num,i):
            num[j] = 1

def solution(nums):
    answer =0
    for i in combinations(nums,3): 
        sum_nums =sum(i)
        if num[sum_nums]==0:
            answer+=1
    return answer

# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x**0.5) + 1):
#         if not x % i:
#             return False
#     return True