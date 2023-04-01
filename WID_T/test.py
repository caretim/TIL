
import sys
input= sys.stdin.readline
for __ in range(int(input().rstrip())):
    a,b = map(int,input().split())
    result = str(a**b) 
    print(result[-1])