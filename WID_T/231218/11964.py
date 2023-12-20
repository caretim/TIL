from collections import deque


T, A, B = map(int, input().split())


visited = [[0] * ((T * 2) + 1) for __ in range(2)]
q = deque()
q.append((0, 0))
re = 0
visited[0][0] = 1
while q:
    po, half = q.pop()
    if po == T:
        print(po)
        exit()
    for i in (po + A, po + B):
        if 0 <= i < ((T * 2) + 1):
            if half == 0:
                if visited[1][i // 2] == 0:
                    visited[1][i // 2] = 1
                    q.appendleft((i // 2, 1))
                if visited[0][i] == 0:
                    visited[0][i] = 1
                    q.appendleft((i, 0))
            elif half == 1:
                if visited[1][i] == 0:
                    visited[1][i] = 1
                    q.appendleft((i, 1))
            if re < i <= T:
                re = i
print(re)


T, A, B = map(int, input().split())

visited = [[0 for _ in range(2)] for _ in range(5000000)]
queue = deque([(0, 0)])
answer = 0
while queue:
    fullness, used = queue.popleft()
    if visited[fullness][used]:
        continue
    visited[fullness][used] = 1
    answer = max(answer, fullness)
    if answer == T:
        break

    if fullness + A <= T:
        queue.append((fullness + A, used))
    if fullness + B <= T:
        queue.append((fullness + B, used))
    if not used:
        queue.append((fullness // 2, 1))

print(answer)
