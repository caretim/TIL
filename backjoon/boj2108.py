#통계학 boj2108



import sys

n= int(input())

nl = []

nd={}

for __ in range(n):
    num=(int(sys.stdin.readline().rstrip()))
    nl.append(num)
    if num not in nd:
        nd[num]=1
    else:
        nd[num]+=1

nl.sort()
nc = int((n-1)/2)





ndm = max(nd,key=nd.get)
nmode =[]
for k in nd:
    if nd.get(k) == ndm:
        nmode.append(k)

nmode.sort()


#모두 더해서 나눈 평균값
print(round(sum(nl)/n))

#중앙값
print(nl[nc])


#최빈값
if len(nmode)>1:
    print(nmode[1])
else:
    print(ndm)



#범위 인덱스
if len(nl)>1:
    m= nl[0]-nl[n-1]
    print(abs(m))
else:
    print(nl[0])



