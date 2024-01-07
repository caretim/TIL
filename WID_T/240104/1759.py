import sys
from itertools import permutations


l, c = map(int, input().split())

alphabet = list(input().split())


result = []
for i in permutations(alphabet, l):
    flag = 1
    a = 0
    b = 0
    for ii in range(1, l):
        if i[ii - 1] >= i[ii]:
            flag = 0
            break
        if i[ii] in ("a", "e", "i", "o", "u"):
            a += 1
        else:
            b += 1
    if i[0] in ("a", "e", "i", "o", "u"):
        a += 1
    else:
        b += 1
    if flag == 1 and a > 0 and b > 1:
        result.append(i)

result.sort()
for r in result:
    print(*r, sep="")


# aeiou = []
# copyAlpha = []
# for a in alphabet:
#         if a == ('a', 'e', 'i', 'o', 'u'):
#             aeiou.append(a)
#         else:
#             copyAlpha.append(a)

# copyAlpha.sort()
