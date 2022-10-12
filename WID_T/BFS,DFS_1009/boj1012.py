# 유기농 배추를 재배하기 위해 필요한  흰 지렁이는 상하좌우로 배추가 존재한다면 이동이 가능
import sys


input = sys.stdin.readline


test_case = int(input())

for test in range(test_case):
    m, n, k = map(int, input().split())

    farm = [[0] * m for __ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    cnt = 0

    for baechu in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    def buy(y, x):
        farm[y][x] = 0
        stack = [(y, x)]
        while stack:
            b = stack.pop()
            for i in range(4):
                ny = b[0] + dy[i]
                nx = b[1] + dx[i]
                # 범위바깥 체크
                if 0 <= nx < m and 0 <= ny < n:
                    # 배추가 있나 체크  있다면 배추 0으로 변경 후 스택에 넣어주기
                    if farm[ny][nx] == 1:
                        farm[ny][nx] = 0
                        stack.append((ny, nx))

    for x in range(m):
        for y in range(n):
            if farm[y][x] == 1:
                buy(y, x)
                cnt += 1

    print(cnt)
