n= input()

nn = n.split('-')

result = 0

if nn[0]=='': # 첫숫자가 음수이고 +연산자가 있을때
    if '+' in nn[1]:
        k = nn[1].split('+')
        result+=sum(map(int,k))
    else: # 첫숫자가 음수이고 연산자 없을때 
        result+=int(nn[1])
    start_number= 2
else: # 음수가 아닐때 첫숫자 미리 더 해주기,
    if '+' in nn[0]:
        k = nn[0].split('+')
        result+=sum(map(int,k))
    else:
        result+=int(nn[0])
    start_number = 1

for i in range(start_number,len(nn)): #첫숫자, 마이너스인지 플러스인지 구분, 
    i = nn[i]
    if '+' in i: # +연산자가 있을 때,
        iii = i.split('+')
        result-=sum(map(int,iii))
    else: # +연산자가 없을 때,
        result-=int(i)
print(result)