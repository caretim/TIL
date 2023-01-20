from collections import deque


def solution(numbers, direction):
    answer = deque(numbers)
    if direction == "right":
        k = answer.pop()
        answer.appendleft(k)
    else:
        k = answer.popleft()
        answer.append(k)
    return list(answer)


print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
