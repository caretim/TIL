def solution(n, lost, reserve):
    check = [1] * (n + 2)
    for l in lost:
        check[l] -= 1
    for r in reserve:
        check[r] += 1
    answer = 0
    for c in range(1, len(check) - 1):  # 첫인덱스와 마지막인덱스 , 첫인덱스와 마지막 인덱스 사용안함, 1,78
        if check[c] == 0:
            if check[c - 1] > 1:
                check[c - 1] -= 1
                check[c] = 1
                answer += 1
            elif c + 1 <= n and check[c + 1] > 1:
                check[c + 1] -= 1
                check[c] = 1
                answer += 1
        else:
            answer += 1
    return answer


lost = [1, 3, 5]
reserve = [2, 4, 6]
n = 6

print(solution(n, lost, reserve))
