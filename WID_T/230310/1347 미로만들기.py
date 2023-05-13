n =int(input())

command=list(input())

# 50, 50으로 시작, y최소 최대 x 최소 최대 구한 후 둘이 빼준 다음에 그 사이의 그래프 표시를 보여주면됨,
matrix = [['#'] * 100 for __ in range(100)]


move= [(1,0),(0,1),(-1,0),(0,-1)]

c = 0

y_min,y_max,x_min,x_max = 50,50,50,50

y, x= 50,50
matrix[y][x] = '.'

for i in command:
    if i == 'R':
        c+=1
    elif i == 'L':
        c-=1
    elif i =='F':
        y,x=y+move[c][0], x+move[c][1] 
        matrix[y][x]='.' # 도착 
        if y_max < y:
            y_max =y
        if y_min > y:
            y_min =y
        if x_min > x:
            x_min =x
        if x_max <x:
            x_max =x 
    if 0>c:
        c =3
    elif 3<c:
        c=0

result = []
for y in range(y_min,y_max+1):
    check = []
    for x in range(x_max,x_min-1,-1):
        check.append(matrix[y][x])
    result.append(check)



for r in result:
    print(*r,sep='')
    


        


