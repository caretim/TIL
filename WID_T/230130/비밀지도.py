def solution(n, arr1, arr2):
    MAP = [[0] * n for __ in range(n)]
    for i in range(n):
        a = bin(arr1[i])[:2]
        b = bin(arr2[i])[:2]
        print(a, b)
    for y in range(n):
        for x in range(n):
            if (y, x) == (" ", " "):
                MAP[y][x] = " "

    answer = []
    return answer


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5
solution(n, arr1, arr2)
