n, nums = int(input()), list(map(int, input().split()))
s = int(input())

for i in range(n):
    max_num = max(nums[i : min(n, i + s + 1)])
    idx = nums.index(max_num)
    for j in range(idx, i, -1):
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
    s -= idx - i
    if s <= 0:
        break

print(*nums)
