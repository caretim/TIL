n = int(input())

visited = list(map(int,input().split()))


diag1 = set()#왼쪽 대각선
diag2 = set()# 오른쪽 대각선
for i in range(len(visited)):
    if visited[i]!=0:
        diag1.add(i+visited[i])
        diag2.add(i-visited[i])

#퀸 대각선 움직임 체크를 어떻게할까
#행에 존재한다면 진행 못하고, 위에서부터 아래로 진행함,
# 왼쪽 대각선 (-1,-1) # 오른쪽 대각선 (-1,1)
#  왼쪽 대각선은 x+y를의 열 , 오른쪽 대각선은 x-y의 열

def queen(now):
    if now ==n:
        print(*visited)
        exit() # 마지막 도달 종료조건
    if visited[now]!=0: #해당 이미 queen 있을 경우
        queen(now+1)
    else: # 해당 행에 퀸이 없을 경우 
        for i in range(n+1):
            if i in visited or (now+i) in diag1 or (now-i)  in diag2:
                continue
            diag1.add(now+i)
            diag2.add(now-i)
            visited[now]=i
            queen(now+1)
            visited[now]=0
            diag1.remove(now+i)
            diag2.remove(now-i)
        
queen(0)
print(-1)