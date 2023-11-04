from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
k =int(input())
nums =[]

for i in range(n):
    nums.append(input().rstrip())

re = set()

for i in permutations(nums, k):
    re.add(''.join(map(str, i)))


print(len(re))