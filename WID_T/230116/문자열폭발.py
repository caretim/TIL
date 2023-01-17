s = input()
bomb = input()

bomb = list(bomb)


result = []

for i in s:
    result.append(i)
    if result[-(len(bomb)) :] == bomb:
        for __ in range(len(bomb)):
            result.pop()


if len(result) == 0:
    print("FRULA")
else:
    print(*result, sep="")
