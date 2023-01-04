
n =input().split('.')

result=[]

check=0
for k in n:
    if  k=='':
        pass
    elif len(k)%4 == 2:
        AAAA = len(k)//4
        result.append('AAAA'*AAAA+'BB')
    elif len(k)%4 == 0 and len(k)>=1:
        AAAA = len(k)//4
        result.append('AAAA'*AAAA)
    else:
        check=1
    result.append('.')
result.pop()

if check==1:
    print('-1')
else:
    print(''.join(result))