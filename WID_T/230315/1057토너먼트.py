n, j, h = map(int, input().split())

cnt = 0

while j != h:
    j -= j // 2
    h -= h // 2
    cnt += 1
print(cnt)
