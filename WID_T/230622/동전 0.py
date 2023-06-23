N, K = map(int, input().split())

matrix =[]

for _ in range(N):
    matrix.append(int(input()))

matrix.sort(reverse=True)


result = 0

for m in matrix:
    if K >= m:
        result += K // m 
        K = K% m 
        if K <= 0: 
       		break
print(result)