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

    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer