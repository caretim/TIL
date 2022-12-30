def solution(s1, s2):
    answer = 0
    l1 = len(s1)
    l2 = len(s2)
    check = s1
    arr = s2
    if l2 < l1:
        check = s2
        arr = s1
    for k in check:
        if k in arr:
            answer += 1
    return answer
