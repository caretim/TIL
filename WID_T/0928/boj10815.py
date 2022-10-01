n = int(input())


sang = list(map(int, input().split()))


m = int(input())

nums = list(map(int, input().split()))


nums.sort()


result = []
for i in range(n):
    start = 0
    end = len(nums) - 1
    mid = start + end // 2
    check = 0
    while start <= end:
        if nums[mid] == sang[i]:
            check = 1
            break
        elif nums[mid] > sang[i]:
            end = mid - 1
        elif nums[mid] < sang[i]:
            start = mid + 1
    nums.append("0")

print(result)
