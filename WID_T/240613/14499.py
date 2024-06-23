
import sys

input =sys.stdin.readline

#주사위 면의 숫자
dice = [0,0,0,0,0,0,0]

# #주사위 움직임 - 첫 인덱스 밑면 위치, 동서북남
# dice_move= {1:[6,4,3,5,2],
#             2:[5,4,3,1,6],
#             3:[4,1,6,5,2],
#             4:[3,6,1,5,2],
#             5:[2,4,3,6,1],
#             6:[1,4,3,2,5], 
# 윗면에 따라 수가 정해지는게 아니라 움직이는 방면에 따라 수가 재정렬됨 
# 따라서 위의 딕셔너리로 숫자를 정하는건 잘못되었음,
# 방향에 따른 수의 위치 변화를 설정해야한다,

def dice_move(order): ####2  
    if order == 1: # 동쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2] # 주사위 변화 4 2 1 6 5 3
    elif order == 2: # 서쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3] # 주사위 변화 3 2 6 1 5 4
    elif order == 3: # 북쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1] # 주사위 변화 5 1 3 4 6 2
    elif order == 4: # 남쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4] # 주사위 변화 2 6 3 4 1 5

dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

def rolling(move_order):
    global dice_top,dice_y,dice_x
    next_y = dice_y+dy[move_order]
    next_x = dice_x+dx[move_order]
    
    if 0<=next_y<n and 0<= next_x<m: 
        dice_move(move_order)
        if matrix[next_y][next_x]:
            dice[5] = matrix[next_y][next_x]
            matrix[next_y][next_x] = 0
        else : 
            matrix[next_y][next_x] = dice[5]
        dice_y = next_y
        dice_x = next_x
        print(dice[0])



#매트릭스의 칸이 0이라면 주사위의 숫자 매트릭스 새겨짐
#매트릭스의 칸이 0이 아니라면 매트리스 칸의 숫자가 주사위로 복사됨 , 매트릭스 칸 0변경
# def rolling(move_oder):
#     global dice_top,dice_y,dice_x

#     next_y = dice_y+dy[move_oder]
#     next_x = dice_x+dx[move_oder]
    
#     if 0<=next_y<n and 0<= next_x<m: 
#         dice_top = dice_move[dice_top][move_oder] # 주사위 윗면 변경, 
#         dice_bottom = dice_move[dice_top][0] # 변경된 주사위 아랫면

#         if matrix[next_y][next_x] !=0: # True일떄
#             dice[dice_bottom] = matrix[next_y][next_x] # 주사위 면 값 변경 
#             matrix[next_y][next_x] = 0 # 매트릭스 값 0 변경


#         elif matrix[next_y][next_x] == 0:   #False 일떄
#             matrix[next_y][next_x]= dice[dice_bottom]
#         dice_y = next_y
#         dice_x = next_x
#         print(dice[dice_top])
#         print(dice,dice_top)
#     else:
#         return # 범위 벗어나면 함수 종료 


    

n,m,x,y,k = map(int,input().split())

matrix = [list(map(int,input().split())) for __ in range(n)]

#주사위 윗면의 숫자

dice_top=1
dice_x = y
dice_y = x 

dice_order =list(map(int,input().split()))
for o in dice_order:
    rolling(o)

    
    