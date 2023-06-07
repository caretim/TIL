n,m= map(int,input().split())
one=[]
six=[]

for __ in range(m):
    s,o =map(int,input().split())
    six.append(s)
    one.append(o)

min_s= min(six)
min_o = min(one)

price=0

if min_s > min_o*6:
    min_s = min_o*6

while n>5:
    n-=6
    price+=min_s

if n != 0:
    if n*min_o<=min_s:
        price+=n*min_o
    else:
        price+=min_s

print(price)


