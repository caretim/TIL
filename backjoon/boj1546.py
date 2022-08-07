n= int(input())

score= list(map(int,input().split()))


ms = max(score)

result=0

for i in score:
    result+= i/ms*100


print(result/n)

