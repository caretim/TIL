hn=int(input())
hcard_ls=[]
hcard_ls=list(map(int,input().split()))

sn=int(input())
scard_ls=[]

scard_ls=list(map(int,input().split()))

hcard_dc={}

for i in hcard_ls:
    if i not in hcard_dc:
        hcard_dc[i] = 1
    else :
        hcard_dc[i] += 1

r= []

for j in scard_ls:
    if j in hcard_dc:
        r.append(hcard_dc.get(j))
    else:
        r.append(0)



print(' '.join(map(str,r)))
