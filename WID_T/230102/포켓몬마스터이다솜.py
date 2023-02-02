
import sys
input = sys.stdin.readline
n,q = map(int,input().split())


dict = {}



for k in range(1,n+1):
    name= input().rstrip()
    dict[str(k)] = name
    dict[name] =k


for __ in range(q):
    question=input().rstrip()
    print(dict[question])

# 밸류 이름 get