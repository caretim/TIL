
n= int(input())

arr =[]
result = []
for __ in range(n):
    arr.append(int(input()))
    
stack = []

cnt = 0

for i in range(1,n+1):
    stack.append(i)
    result.append('+')
    while True:
        if len(stack)==0:
            break
        if stack[-1] == arr[cnt]:
            stack.pop()
            result.append('-')
            cnt+=1
        else:
            break

if len(stack) !=0:
    print('NO')
else:
    for i in result: print(i)

    


        
    
stack = []
