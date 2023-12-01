import sys

input = sys.stdin.readline


while True:
    count = [0] * 10001

    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    for __ in range(n):
        member = list(map(int, input().split()))
        for i in member:
            count[i] += 1

    first = count.index(max(count))  # 최대값 인덱스 확인,
    count[first] = 0
    secondNum = max(count)
    result = []
    for i in range(len(count)):
        if secondNum == count[i]:
            result.append(i)
    print(*result)
