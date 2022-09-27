n = int(input())


nlist = list(map(int, input().split()))

nlist.sort()

maxn = int(input())

# halfn = maxn - maxn // 2

cnt = 0

i = 0
j = n - 1
# 2개의 번호만 찾으면 됨,

while i > j:
    if nlist[i] + nlist[j] < maxn:
        i += 1
    elif nlist[i] + nlist[j] > maxn:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1

print(cnt)
