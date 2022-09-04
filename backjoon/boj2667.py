n=int(input())

matrix=[list(map(int,input())) for __ in range(n)]

dy=[0,0,-1,1]
dx=[-1,1,0,0]

 
def bundle(y,x):
    cnt=1
    matrix[y][x]=0
    stack=[]
    stack.append((y,x))
    while stack:
        st = stack.pop()
        for i in range(4):
            ny= st[0]+dy[i]
            nx= st[1]+dx[i]
            if ny<0 or ny>=n or nx<0 or nx>=n :
                continue
            elif matrix[ny][nx]==1:
                matrix[ny][nx]=0
                cnt+=1
                stack.append((ny,nx))
    return cnt



result =[]

for y in range(n):
    for x in range(n):
        if matrix[y][x]==1:
            re = bundle(y,x)
            result.append(re)

result.sort()

print(len(result))
for r in result:
    print(r)