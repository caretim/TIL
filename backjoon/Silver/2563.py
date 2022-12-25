matrix = [[0]*100 for __ in range(100)]


n= int(input())

for __ in range(n):
    j,i = map(int,input().split())
    for y in range(j,j+10):
        for x in range(i,i+10):
            matrix[y][x] =1

result =0

for y in range(100):
    for x in range(100):
        if matrix[y][x] ==1:
            result+=1

print(result)