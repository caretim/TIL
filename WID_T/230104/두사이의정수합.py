def solution(a, b):
    answer = 0
    if a == b:
        answer = a

    elif a > b:
        a1 = b
        b1 = a

        for k in range(a1, b1 + 1):
            answer += k
    else:
        for k in range(a, b + 1):
            answer += k

    return answer


print(solution(5, 3))
