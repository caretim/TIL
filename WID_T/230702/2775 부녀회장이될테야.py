
for tc in range(int(input())):
    k = int(input())
    n = int(input())

    matrix = [[0]*(15)for __ in range(15)]

    for i in range(15):
        matrix[0][i]=i

    for i in range(1,k+1):
        for j in range(n+1):
            matrix[i][j]=sum(matrix[i-1][0:j+1])



    print(matrix[k][n])