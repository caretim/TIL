import sys

input = sys.stdin.readline


for tc in range(int(input())):
    n = int(input())

    numbers = []
    for __ in range(n):
        numbers.append(input().rstrip())

    numbers.sort()
    # 순서대로 정렬시키기,

    result = "YES"

    for i in range(len(numbers) - 1):
        if (
            numbers[i] in numbers[i + 1][: len(numbers[i])]
        ):  # 현재 인덱스 번호가 다음 인덱스의 번호에 존재하는지 체크, 정렬했기에, 바로 뒤로 검사가능,
            result = "NO"
            break

    print(result)
