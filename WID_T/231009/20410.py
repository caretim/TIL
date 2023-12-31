m, seed, x1, x2 = map(int, input().split())


# m = 100이하
for a in range(100):
    for c in range(100):
        if x1 == (a * seed + c) % m:
            if x2 == (a * ((a * seed + c) % m) + c) % m:
                print(a, c)
                exit()
