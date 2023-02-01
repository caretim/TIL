from collections import deque


ingredient=[2, 1, 1, 2, 3, 1, 2, 3, 1]
def solution(ingredient):
    burger=[1,2,3,1]
    answer = 0
    q = deque()
    for k in ingredient:
        q.append(k)
        if len(q) >=4:
            check=0
            for i in range(1,5):
                if q[-i]!=burger[-i]:
                    check=1
            if check==0:
                answer+=1
                for __ in range(4):
                    q.pop()

    return answer





print(solution(ingredient))

# result= [0,0,0,0]

# def solution(ingredient):
#     answer = 0
#     cursor=0
#     for k in reversed(ingredient):
#         result[k]+=1
#     print(result)
#     # 2/1/1 뺴주는데 , 종료조건을 어떻게 걸어주지?
#     while result[1]>2 and result[2]>1 and result[3]>1:
#         result[1]-=2
#         result[2]-=1
#         result[3]-=1
#         answer+=1
    
#     return answer

# print(solution(ingredient))