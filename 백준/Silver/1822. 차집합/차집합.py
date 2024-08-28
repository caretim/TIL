import sys
input =sys.stdin.readline


dict = {}

la,lb = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))


for i in a:
    dict[i]=1


for i in b:
    if i in dict:
       dict[i]=0

result= []
for i in a:
    if dict[i]==1:
        result.append(i)

result.sort()
if len(result):
    print(len(result))
    print(*result)
else:
    print(0)
