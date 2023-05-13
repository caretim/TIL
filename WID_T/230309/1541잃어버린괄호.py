
#최종본

n= input()

nn = n.split('-')

result = 0
flag=0
if nn[0]=='': # 첫숫자가 음수이고 +연산자가 있을때 
    check =1

if '+' in nn[flag]:
    k = nn[flag].split('+')
    result+=sum(map(int,k))
else: 
    result+=int(nn[flag])

for i in range(flag+1,len(nn)): #첫숫자, 마이너스인지 플러스인지 구분, 
    i = nn[i]
    if '+' in i: # +연산자가 있을 때,
        iii = i.split('+')
        result-=sum(map(int,iii))
    else: # +연산자가 없을 때,
        result-=int(i)

print(result)


# flag = True # 괄호 열림 닫힘 표시 
# for ii in range(len(n)):
#     i = n[ii]
#     if i!='-':
#         result+=i
#     else:
#         if flag == True:
#             result+=i
#             result+='('
#             flag= False
#         elif flag == False:
#             result+=')'
#             result+=i
#             result+='('
#     if ii == len(n)-1 and flag==False:
#         result+=')'

# print(eval(result)) # 0시작일 때 어떻게처리? 흠  받을때 + -부호로 스플릿해서 처리?

# 마이너스로 스플릿해서, 공백이 등장하면 뒷자리 더해준다, 

    

# n= input()

# nn = n.split('-')

# result = 0
# flag=0
# if nn[0]=='': # 첫숫자가 음수이고 +연산자가 있을때 
#     check =1

# if '+' in nn[flag]:
#     k = nn[flag].split('+')
#     result+=sum(map(int,k))
# else: 
#     result+=int(nn[flag])


# else: # 음수가 아닐때 첫숫자 미리 더 해주기,
#     if '+' in nn[0]:
#         k = nn[0].split('+')
#         result+=sum(map(int,k))
#     else:
#         result+=int(nn[0])
#     start_number = 1

# for i in range(flag+1,len(nn)): #첫숫자, 마이너스인지 플러스인지 구분, 
#     i = nn[i]
#     if '+' in i: # +연산자가 있을 때,
#         iii = i.split('+')
#         result-=sum(map(int,iii))
#     else: # +연산자가 없을 때,
#         result-=int(i)

# print(result)
    

