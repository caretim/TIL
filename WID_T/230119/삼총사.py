from itertools import combinations


def solution(number):
    answer = 0
    c = combinations(number, 3)
    for i in c:
        if sum(i) == 0:
            answer += 1

    return answer


number = [-2, 3, 0, 2, -5]


print(solution(number))
