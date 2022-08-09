from collections import Counter
import sys

# sys.stdin = open('input.txt')
words = input()
words = words.replace('\n', '').replace(' ', '')

alpha_list = Counter(words)
keys = []
max_often = max(alpha_list.values())
for key,value in alpha_list.items():
    if value == max_often:
        keys.append(key)

keys.sort()
print(*keys,sep='')