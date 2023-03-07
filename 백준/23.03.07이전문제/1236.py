n,m= map(int,input().split())



matrix=[list(input()) for __ in range(n)]


xcnt=0
ycnt=0

# X축 검사
for xmatrix in matrix:
    if 'X'  in xmatrix:
        xcnt+=1


#Y축 검사

for x in range (m):
    for y in range(n):
       if matrix[y][x] == 'X':
            ycnt+=1
            break


rl =[n-xcnt,m-ycnt]

result= max(rl)

print(result)
    




        
        
    
    


