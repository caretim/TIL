


n= list((input().split()))


# n= input()
# N =n.replace(' ','change')

# result = list(N.split('change'))
# print (result)
for i in n:
    if i =='':
        n.remove('')
    if i ==' ':
        n.remove(' ')


print (len(n))