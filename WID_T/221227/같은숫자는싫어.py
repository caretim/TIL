arr = [1, 1, 3, 3, 0, 1, 1]


def solution(arr):
    answer = []
    check = -1
    for i in arr:
        if i != check:
            answer.append(i)
            check = i
    return answer


print(solution(arr))
