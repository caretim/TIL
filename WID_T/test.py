import sys
from itertools import combinations

input = sys.stdin.readline

n= int(input())

taste = []

for __ in range(n):
    taste.append(list(map(int,input().split())))

com = []
for i in range(1, n+1):
    com.append(combinations(taste, i))

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