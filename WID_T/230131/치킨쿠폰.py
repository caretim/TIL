def solution(chicken):
    answer = 0
    while chicken >= 10:
        l = chicken % 10
        chicken = chicken // 10
        answer += chicken
        chicken += l
    return answer


chicken = 130
print(solution(chicken))
