
n1=input()
n2=input()
n3=input()
n4=input()
n5=input()

lsn1=list(str(n1))
lsn2=list(str(n2))
lsn3=list(str(n3))
lsn4=list(str(n4))
lsn5=list(str(n5))


char = []

for i in range(15):
    if len(lsn1) >= 1 :
        char.append(lsn1.pop(0))
    if len(lsn2) >= 1 :
        char.append(lsn2.pop(0))
    if len(lsn3) >= 1 :
        char.append(lsn3.pop(0))
    if len(lsn4) >= 1 :
        char.append(lsn4.pop(0))
    if len(lsn5) >= 1 :
        char.append(lsn5[0])
        lsn5.remove(lsn5[0])

print (''.join(char))




