



nsum=0
index=0
for i in range(1,6):
    n= list(map(int,input().split()))
    if nsum< sum(n):
        nsum=sum(n)
        index= i
print (index,nsum)

