def solution(k, d):
    num = []
    for i in range(0, d + 1, k):
        for j in range(0, d + 1, k):
            if i**2 + j**2 < d:
                num.append((i, j))
    print(num)
    answer = 0
    return answer


print(solution(2, 5))
