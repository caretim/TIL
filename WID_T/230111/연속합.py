n = int(input())

dp = []

num_list = list(map(int, input().split()))

count = 0

max_num = 0

for num in num_list:
    count += num
    if count > max_num:
        max_num = count
    if count < 0:
        dp.append(count)
        count = 0
    else:
        dp.append(count)

print(max(dp))
