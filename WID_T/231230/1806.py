import sys


n, s = map(int, input().split())


nums = list(map(int, input().split()))

nums.append(0)


l = 0

r = 0
total = nums[0]
result = 99999999

cnt = 1

while r < n:
    if total < s:
        r += 1
        cnt += 1
        print(r)
        total += nums[r]

    else:
        result = min(result, cnt)
        total -= nums[l]
        cnt -= 1
        l += 1


if result == 99999999:
    print(0)
else:
    print(result)
