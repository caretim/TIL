

n=input()


nlist=[]

for e in n:
    nlist.append(int(e))


nlist.sort(reverse=True)

print (*nlist,sep='')
