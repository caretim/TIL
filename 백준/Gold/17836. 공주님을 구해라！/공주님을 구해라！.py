import sys

input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n, m, t = map(int, input().split())

matrix = [list(map(int, input().split())) for __ in range(n)]

check = [[0] * m for __ in range(n)]

result = 100000000
g_result = 100000000


# 그람 없이 지나다닐때 1 있을때 2
# 진행되는 동시탐색은 같은 cnt횟수를 가지고 있음.
def bfs(n, m):
    cnt = 0
    q = [(0, 0)]
    check[0][0] = 1
    global result
    global g_result
    while q:
        temp = []
        cnt += 1
        for y, x in q:
            if (y, x) == (n - 1, m - 1):
                result = cnt - 1
                break
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if (
                    0 <= ny < n and 0 <= nx < m
                ):  ## 그람을 발견했을때는? #모든 벽 뚫기 가능함 그래서 그냥 직선거리 계산하기
                    if check[ny][nx] == 0 and matrix[ny][nx] == 2:  # 그람주워먹었을때 방문리스트2
                        g_result = cnt + ((n - 1) - ny) + ((m - 1) - nx)
                        check[ny][nx] = 1
                        temp.append((ny, nx))
                    elif check[ny][nx] == 0 and matrix[ny][nx] == 0:
                        temp.append((ny, nx))
                        check[ny][nx] = 1

        # 그냥 길 지나다닐때 방문리스트1 그람먹으면 역주행함 메모리초과 .. 흠 ..
        # 숫자로 비교하려니 역주행 또는 그람을 잃어버리는 경우가 생김,
        else:
            q = temp
            continue
        break


bfs(n, m)
# print(result, g_result)
result = min(result, g_result)
print(result if result <= t else "Fail")