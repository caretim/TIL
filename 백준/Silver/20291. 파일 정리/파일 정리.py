import sys

input = sys.stdin.readline

n = int(input())

dict = {}

for _ in range(n):
    f1, f2 = input().rstrip().split(".")
    if f2 in dict:
        dict[f2] += 1
    else:
        dict[f2] = 1

for k, v in sorted(dict.items()):
    print(k, v)
