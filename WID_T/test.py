
result = sys.maxsize
for line in com:
    for each in line:
        sour = 1
        bitter = 0
        for e in each:
            sour *= e[0]
            bitter += e[1]

        result = min(result, abs(sour - bitter))

print(result)

