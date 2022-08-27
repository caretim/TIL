


dy=[-1,-1,-1,0,0,1,1,1]
dx=[-1,0,1,-1,1,-1,0,1]

def fl (y,x):
    land[y][x]=0
    stack=[]
    stack.append((y,x))
    while stack:
        k = stack.pop()
        for i in range(8):
            ny = dy[i]+k[0]
            nx = dx[i]+k[1]
            if ny>=n or ny <0 or nx >= m or nx <0:
                continue
            if land[ny][nx]==1:
                land[ny][nx]=0
                stack.append((ny,nx))
    return 1


while True:
    m, n = map(int,input().split())
    if n==0 and m ==0:
        break
    land=[list(map(int,input().split())) for __ in range(n)]
    cnt=0
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1:
                fl(y,x)
                cnt+=1
    print(cnt)


    