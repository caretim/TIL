n,m= map(int,input().split())


matrix =[list(input()) for __ in range(n)]


white = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

black = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

#한줄씩 읽기  8x8가져오기 

def checker(y,x,ly,lx):
    return_list=[]
    count=0
    check= 0
    if matrix[y][x] =='W':
        check=1
    elif matrix[y][x] =='B':
        check=2
    cursor = check
    for ny in range(y,ly):
        check_list=[]
        for nx in range(x,lx):
            check_list.append(matrix[ny][nx])
        if cursor == 1 :
            for i in range(8):
                if check_list[i] != white[i]:
                    count+=1
            cursor = 2
        else:
            for i in range(8):
                if check_list[i] != black[i]:
                    count+=1
            cursor = 1
    return_list.append(count)

    count=0
    check= 0
    if matrix[y][x] =='B':
        check=1
    elif matrix[y][x] =='W':
        check=2
    cursor = check
    for ny in range(y,ly):
        check_list=[]
        for nx in range(x,lx):
            check_list.append(matrix[ny][nx])
        if cursor == 1 :
            for i in range(8):
                if check_list[i] != white[i]:
                    count+=1
            cursor = 2
        else:
            for i in range(8):
                if check_list[i] != black[i]:
                    count+=1
            cursor = 1
    return_list.append(count)

    return min(return_list)



result =[]
for y in range(n):
    for x in range(m):
        ly = y+8
        lx = x+8
        if 0<= ly <=n and 0<= lx <=m:
            result.append(checker(y,x,ly,lx))

print(min(result))