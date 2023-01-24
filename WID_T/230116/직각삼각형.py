while True:

    a, b, c = map(int, input().split())
    num_list = [a, b, c]
    if sum(num_list) == False:
        break
    m = max(num_list)
    num_list.remove(m)

    if num_list[0] ** 2 + num_list[1] ** 2 == m**2:
        print("right")
    else:
        print("wrong")
