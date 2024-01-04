# import sys
# from itertools import permutations


# l, c = map(int, input().split())

# alphabet = list(input().split())


# result = []
# for i in permutations(alphabet, l):
#     flag = 1
#     a = 0
#     b = 0
#     for ii in range(1, l):
#         if i[ii - 1] >= i[ii]:
#             flag = 0
#             break
#         if i[ii] in ("a", "e", "i", "o", "u"):
#             a += 1
#         else:
#             b += 1
#     if i[0] in ("a", "e", "i", "o", "u"):
#         a += 1
#     else:
#         b += 1
#     if flag == 1 and a > 0 and b > 1:
#         result.append(i)

# result.sort()
# for r in result:
#     print(*r, sep="")



import sys
input = sys.stdin.readline

l, c = map(int, input().split())
arr = sorted(list(input().split()))
def dfs(s):
    if len(s) == l:
        a, b = 0, 0
        for m in s:
            if m in "aeiou":
                a += 1
            else:
                b += 1
        if a >= 1 and b >= 2:
            return print("".join(s))
        return
    for v in arr:
        if v > s[-1]:
            s.append(v)
            dfs(s)
            s.pop()
for i in range(c - l + 1):
    dfs([arr[i]])