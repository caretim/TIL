import sys

input = sys.stdin.readline  #

n = int(input())

num_list = list(map(int, input().split()))
num_set = list(set(num_list))
num_set.sort()

print(*num_set)
