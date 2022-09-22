import sys

# n= int(input())

matrix = [list(map(int,input().split())) for __ in range(9)]


check=0

for matrix_x in matrix:
    nums =[1,2,3,4,5,6,7,8,9]
    for n in matrix_x:
        if n not in nums:
            check=1
            break
        else:
            nums.remove(n)
             


for x in range(9):
    nums =[1,2,3,4,5,6,7,8,9]
    for y in range(9):
        if matrix[x][y] not in nums:
            check=1
        else:
            nums.remove(matrix[x][y])


print(check)