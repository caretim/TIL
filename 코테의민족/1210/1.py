# https://school.programmers.co.kr/learn/courses/30/lessons/70128





def solution(a, b):
    answer = 0
    ab = zip(a,b)
    n = len (a)
    for i,j in ab:
        answer = answer+(i*j)

    return answer