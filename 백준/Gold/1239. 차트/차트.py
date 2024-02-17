#https://www.acmicpc.net/problem/1239
#차트


import sys
from itertools import permutations

input = sys.stdin.readline


#원의 중심을 가로지르기 위해선, 합이 50인 원소의 갯수 찾기 ,
#50을 이루는 원소중 대칭값이 되는 개수가 가장 적은 집합 원소의 개수가 정답,

n = int(input())

per_Dict ={}

per = list(map(int,input().split()))

all_Case = list(permutations(per)) # 동일한 비율이라는걸 알 수 있는 방법, 

result = 0
for case in all_Case:
    check_list=[]
    sum_i = 0
    for c in case:
        sum_i+=c
        check_list.append(sum_i)
    cnt = 0
    for i in check_list:
        if i+50 in check_list: # 모든 조합의 경우수 사용 누적합을 통해 대칭을 이루는 값 찾기 ,
            cnt+=1
    result =max(cnt,result)

print(result)

# if per[n-1]>50:
#     print(0)
#     exit()

# for i in per:
#     if i not in per_Dict:
#         per_Dict[i]=1
#     else:
        # per_Dict[i]+=1



#누적합으로 원소의 개수 많이 나올떄,
# 10 40 10 40 배열
# 10 50 60 100 누적합
# 40 10 10 40 배열
# 40 50 60 100 누적합
# 10 40 40 10 
# 10 50 90 100 누적합
# 40 40 10 10
# 40 80 90 100


  
# #맨 앞 인덱스에서 맨뒤에서 값을 하나씩 더하며 50이 되는 값 확인하고 그 값들을 뺀 대칭 값 찾기
# for i in range(n):
#     q = deque()
#     for j in range(n-1,i,-1):
#         k = per[i]+sum(q)+per[j]
#         if  k== 50:
#             q.append(per[j])
#             break
#         elif k<50:
#             q.append(per[j])
#         elif k>50: # 이경우가 나올까? 모든 값의 조합을 찾아야하는데, 연달아 더한값은 효과가없음
#             q.popleft()
#             q.append(per[j])

#10,15,5,20,20,10,10,10
    

        




