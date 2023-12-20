import sys
from collections import defaultdict

input = sys.stdin.readline

dict = defaultdict(int)
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    dict[tree] += 1
    n += 1

result = list(dict.keys())

result.sort()

for t in result:
    print("%s %.4f" % (t, dict[t] * 100 / n))  # 소수점4자리까지.
