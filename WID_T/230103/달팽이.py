import pprint

t = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for tc in range(1,t+1):
    n = int(input())

    matrix = [[0]*n for __ in range(n)]
   
    cnt=1
    matrix[0][0]=cnt
    stack=[(0,0)]
    d =0
    while n*n > cnt: 
        if d==4:
            d=0
        y,x = stack.pop()
        ny = y+dy[d]
        nx = x+dx[d]

        if 0<=ny<n and 0<=nx<n and matrix[ny][nx]==0:
                cnt+=1
                matrix[ny][nx]=cnt
                stack.append((ny,nx))

        else:
            stack.append((y,x))
            d+=1
    print(f'#{tc}')
    for k in matrix:
        print(*k)
        
        


    