from collections import deque


def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    answer = 0
    dp = [0]*(y+1)
    # x -> y로 변환하기 위핸 최소 연산 횟수 x*n,x*2,x*3
    while q:
        x, j = q.popleft()
        if x == y:
           answer =j
           break
        for k in (x + n, x * 2, x * 3):
            if k < y + 1:
                if dp[k]==0:
                    print("큐삽입")
                    q.append((k, j + 1))
                    dp[k]=1
    print(dp)
    if answer == 0:
        answer=-1
    return answer

print(solution(10,40,5))