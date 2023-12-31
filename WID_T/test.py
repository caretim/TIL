n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0 for _ in range(100)]


start = 0
end = 0
partSum = arr[0]
length = 1

result = 999999

while end <= n:
    if partSum < m:
        end += 1
        length += 1
        partSum += arr[end]
    else:
        result = min(result, length)
        start += 1
        partSum -= arr[start - 1]
        length -= 1
    print(arr)

print(result)
