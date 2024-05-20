#n개의 퀸을 둘 수 있는 경우의 수 찾기


#대각선 체크
diag1 = set() # 행+열
diag2 = set() # 행-열

n= int(input())

visited = [0]*(n+1)
result = 0

def traking(depth):
    global result
    if depth == n+1:
        result+=1
        return
    for i in range(1,n+1):
        if i in visited or depth+i in diag1 or depth-i in diag2:
            continue
        diag1.add(depth+i)
        diag2.add(depth-i)
        visited[depth]=i
        traking(depth+1)
        diag1.remove(depth+i)
        diag2.remove(depth-i)
        visited[depth]=0

traking(1)
print(result)

