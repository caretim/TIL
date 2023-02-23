n = int(input())
num = list(map(int, input().split()))


arr = {}

for k in num:
    arr[k] = 1

m = int(input())

m_num = list(map(int, input().split()))

for j in m_num:
    if j in arr:
        print(1)
    else:
        print(0)
