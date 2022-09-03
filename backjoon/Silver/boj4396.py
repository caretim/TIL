# -*- coding: utf-8 -*- 
# # 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	2120	677	528	30.805%
# 문제
# 지뢰찾기는 n × n 격자 위에서 이루어진다. m개의 지뢰가 각각 서로 다른 격자 위에 숨겨져 있다. 플레이어는 격자판의 어느 지점을 건드리기를 계속한다. 지뢰가 있는 지점을 건드리면 플레이어가 진다. 지뢰가 없는 지점을 건드리면, 그곳의 상하좌우 혹은 대각선으로 인접한 8개의 칸에 지뢰가 몇 개 있는지 알려주는 0과 8 사이의 숫자가 나타난다. 완전히 플레이되지 않은 게임에서 일련의 동작이 아래에 나타나 있다.

# 여기서, n은 8이고, m은 10이며, 빈 칸은 숫자 0을 의미하고, 올라가 있는 칸은 아직 플레이되지 않은 위치이며, 별표 모양(*)과 닮은 그림은 지뢰를 의미한다. 맨 왼쪽의 그림은 일부만이 플레이된 게임을 나타낸다. 첫 번째 그림에서 두 번째 그림으로 오면서, 플레이어는 두 번의 이동을 시행해서, 두 번 다 안전한 곳을 골랐다. 세 번째 그림을 볼 때 플레이어는 운이 썩 좋지는 않았다. 지뢰가 있는 곳을 골라서 게임에서 졌다. 플레이어는 m개의 열리지 않은 칸을 남길 때까지 계속해서 안전한 곳을 고르면 이긴다. 그 m개의 칸은 반드시 지뢰이다.

# 당신이 할 일은 일부가 플레이된 게임의 정보를 읽어 해당하는 격자를 출력하는 것이다.



n = int(input())

bomb_m=[list(input()) for __ in range(n)]

play_m=[list(input()) for __ in range(n)]
result_m=[['.']*n for __ in range(n)]

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]

def bombs(y,x): # 주변 지뢰 탐색하는 함수
    bomb=0
    for i in range(8):
        if  0 <= y+dy[i] <= n-1 and 0 <= x+dx [i] <= n-1 :
            if bomb_m[y+dy[i]][x+dx[i]] == '*':
                bomb+=1
    return bomb
        
for x in range(n):  #지뢰판을 순회하며 플레이 상황 확인 
    for y in range(n):
        if play_m[y][x]=='x': # 플레이어가 칸을 열었을때 
            if bomb_m[y][x]=='.': # 지뢰가 없을 때
                play_m[y][x] = bombs(y,x)
            elif bomb_m[y][x] == '*':# 지뢰가 있을 때
                for j in range(n):
                    for k in range(n):
                        if bomb_m[j][k] =='*':
                            play_m[j][k] ='*'
                    
                



for result in play_m:
    print(*result,sep='')



