h1,m1,s1= map(int,input().split(':'))

h2,m2,s2= map(int,input().split(':'))

h=h2-h1 
m=m2-m1
s=s2-s1

while True:
    if s >= 60:
        m+=1
        s-=60
    elif s <0:
        m-=1
        s+=60
    else:
        break
while True:
    if m >= 60:
        h+=1
        m-=60
    elif m <0:
        h-=1
        m+=60
    else:
        break
while True:
    if h >= 24:
        h-=24
    elif h < 0:
        h+=24
    else:
        break

print('%02d:%02d:%02d'% (h,m,s))