
import sys


n=int(input())

nlist=[]


for __ in range(n):
    num=int(sys.stdin.readline().rstrip())
    nlist.append(num)

nlist.sort()

for result in nlist:
    print(result)