import sys
input = sys.stdin.readline

def find(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            find(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
cnt = 0

find(k, arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1
print(cnt)