matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


n=3 

result= [[0]*n for __ in range(n)]

for y in range(n):
    for x in range(n):
        result [y][x] = matrix[n-y-1][x]

print(result)