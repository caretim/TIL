arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]


for i in range(10, 101):
    arr.append((arr[i - 2] + arr[i - 3]))


for __ in range(int(input())):
    print(arr[int(input()) - 1])


# i = i-2 i-3
