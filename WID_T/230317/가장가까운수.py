# https://school.programmers.co.kr/learn/courses/30/lessons/120890


def solution(array, n):
    array.sort()
    r = 2e9
    answer = 0
    for i in array:
        if r > abs(n - i):
            r = abs(n - i)
            answer = i

    return answer
