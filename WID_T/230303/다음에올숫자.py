# https://school.programmers.co.kr/learn/courses/30/lessons/120924
def solution(common):
        k = common[-1]-common[-2] 
        if k == common[-2]-common[-3]:
            answer = common[-1]+k
        else:
            answer = common[-1]*(common[-1]//common[-2])
        return answer