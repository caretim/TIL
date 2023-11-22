from itertools import permutations


n = int(input())


result = permutations(range(1, n+1), n)


for r in result:
    for i in r:
        print(i, end=" ")
    print()