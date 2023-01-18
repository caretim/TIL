import math


# # 최대공약수
# def solution(n, m):
#     answer = []
#     check_list=[]
#     l,h =max(n,m),min(n,m)
#     for num in h:
#         if num%l==0:
#             check_list.append(num)
#     answer.
#     return answer


def solution(n, m):
    answer = []
    gcd = math.gcd(n, m)
    answer.append(gcd)
    answer.append(n * m // gcd)

    return answer


n, m = 2, 5
print(solution(n, m))
