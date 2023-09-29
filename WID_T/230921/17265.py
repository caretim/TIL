import sys
input = sys.stdin.readline

n= int(input())

INF = sys.maxsize

move = [(0,1),(1,0)] # 아래,오른쪽

matrix = [list(input().rstrip().split()) for __ in range(n)]
max_dp = [[-INF for _ in range(n)] for _ in range(n)]
min_dp = [[INF for _ in range(n)] for _ in range(n)]
max_dp[0][0] = int(matrix[0][0])
min_dp[0][0] = int(matrix[0][0])
# rmax =-INF
# rmin = INF

def checking(x,y,oper):
    for i in range(2):
        nx,ny = x+move[i][0],y+move[i][1]
        if 0<=nx<n and 0<=ny<n:
            if matrix[nx][ny].isdigit():
                max_dp[nx][ny] = max(max_dp[nx][ny], eval(str(max_dp[x][y])+str(oper)+str(matrix[nx][ny])))
                min_dp[nx][ny] = min(min_dp[nx][ny], eval(str(min_dp[x][y])+str(oper)+str(matrix[nx][ny])))
                checking(nx,ny,'')
            else:
                if matrix[nx][ny]=='+':
                    new_oper ='+'
                elif matrix[nx][ny]=='-':
                    new_oper ='-'
                elif matrix[nx][ny]=='*':
                    new_oper ='*'
                max_dp[nx][ny] = max_dp[x][y]
                min_dp[nx][ny] = min_dp[x][y]
                checking(nx,ny,new_oper)
        
        

checking(0,0,'')
print(max_dp[n-1][n-1], min_dp[n-1][n-1])



