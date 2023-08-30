
n= int(input())

result = ''

Files=[]

for __ in range(n):
    file = input()
    Files.append(file)


char = len(Files[0])


for i in range(char):
    check=0
    for j in range(n):
        if Files[j][i]!=Files[0][i]:
            check=1
            break
    if check ==0:
        result+=Files[0][i]
    else:
        result+='?'
print(result)