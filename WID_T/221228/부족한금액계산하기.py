# https://school.programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    answer = -1
    for k in range(1, count + 1):
        money -= price * k

    if money >= 0:
        answer = 0
    else:
        answer = abs(money)

    return answer
