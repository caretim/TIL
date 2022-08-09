
Q1=0
Q2=0
Q3=0
Q4=0
AXIS=0

n= int(input())

for __ in range(n):
    x,y= map(int,input().split())
    if 0<x and 0<y:
        Q1+=1
    elif 0<x and 0>y:
        Q4+=1
    elif 0>x and 0>y:
        Q3+=1
    elif 0>x and 0<y:
        Q2+=1
    elif x==0 or y==0:
        AXIS+=1

print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AIXS: {AXIS}')
