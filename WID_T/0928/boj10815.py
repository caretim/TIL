n = int(input())


sang = list(map(int, input().split()))


m = int(input())

nums = list(map(int, input().split()))

sang.sort()

result = []

for i in range(m):
    start = 0
    end = len(sang) - 1
    check = 0
    while start <= end:
        mid = (start + end) // 2
        if sang[mid] == nums[i]:
            check = 1
            break
        elif sang[mid] > nums[i]:
            end = mid - 1
        elif sang[mid] < nums[i]:
            start = mid + 1
    print(check, end=" ")


# n = int(input())
# N = list(map(int, input().split()))
# N = sorted(N)
# m = int(input())
# M = list(map(int, input().split()))

# for i in M:
#     low, high = 0, n - 1
#     check = 0
#     while low <= high:
#         mid = (low + high) // 2
#         if N[mid] > i:
#             high = mid - 1
#         elif N[mid] < i:
#             low = mid + 1
#         else:
#             check = 1
#             break
#     print(check, end=" ")
