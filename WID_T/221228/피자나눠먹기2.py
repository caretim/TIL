def solution(n):
    for i in range(1, 101):
        pizza = i * 6
        if pizza % n == 0:
            answer = i
            break
    return answer


# 6의배수중 n으로 나눴을때 나눠지는 수
print(solution(int(input())))
