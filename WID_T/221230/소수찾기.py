# https://school.programmers.co.kr/learn/courses/30/lessons/12921


def solution(n):
    # 소수는 1과 본인의 수만 나눠지는 수 N제곱근보다 작은 수 중   N제곱근의 약수가 없다면 N의 약수도 없음
    answer = 0
    for j in range(2, n + 1):
        check = 0
        for i in range(2, int(j ** (1 / 2) + 1)):
            if j % i == 0:
                check += 1
                break
        if check == 0:
            answer += 1
    return answer


print(solution(10))
