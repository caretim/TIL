# def solution(n):
#     answer = []
#     count = 0
#     while n:
#         n = n // 10
#         count += 1
#     for i in range(count, 0, -1):
#         answer.append(i)
#     return answer


def solution(n):
    answer = []
    k = str(n)
    num_len = len(k)
    for i in range(num_len - 1, -1, -1):
        answer.append(int(k[i]))
    return answer


def digit_reverse(n):
    return list(map(int, reversed(str(n))))


print(solution(123450000))
