n = input()

result = []



for i in range(len(n)):
    result.append(n[i:])

result.sort()

for i in result:
    print(i)