

# 1 2 3 4 5 6 7
# 2 4 6 8 10 12 14
# 3 6 9 12 15 18 21


# 1 2 3 4 5 
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25



n, k = int(input()), int(input())

start, end = 1, k
result = 0

while start <= end:
    mid = (start + end) // 2

    checker = 0
    for i in range(1, n+1):
        checker += min(mid//i, n) 

    if checker >= k: 
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)