
dy = [0,0,1,-1]
dx = [1,-1,0,0]

matrix = [list(input()) for i in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time =0

# 재귀로 푸는게 마음 편할거같은데 
# 큐로 구현해서 한 경우 탐색시 주변 같은색상 탐지, 
# 1.해당 위치에 뿌요가 존재한다면 주변 탐색 ->  연속해서 다 탐색하며 리스트에 넣기 -> q말고 dfs로 진행 
# 2. 리스트가 4가 넘는다면 리스트에 들어있는 주소값들을 지우며 좌표를 당겨온다 (어떻게?)
# 3. 부서지고 중력적용은 어떻게 시켜줄까?
# 3-1. 부순후에 밑의 좌표가 . 일떄 위의 값들을 당겨오는 로직
# 3-2. 부술 때 

def playing():
    boom=0
    check = [[0]*6 for __ in range(12)]
    for y in range(12):
        for x in range(6):
            if check[y][x] ==0 and matrix[y][x] in ["Y","G","R","P","B"]:
                if find(y,x,matrix[y][x]) == True:
                    boom=1
    if boom ==1:
        playing()
    else:
        return(time)



def find(y,x,p):
    global check
    pang = 0
    stack =list((y,x))
    pang_lsit =[]
    while stack :
        stack.pop((y,x))
        for i in range(4):
            ny,nx=y+ny[i],x+nx[i]
            if 0<=ny<12 and 0<=nx<6 :
                if check[ny][nx]==0 and matrix[ny][nx]==p:
                    stack.append((ny,nx))
                    pang_lsit.append((ny,nx))
                    pang+=1
    if pang >= 4:
        #뿌요 지우고 중력적용 y축으로 값을 어떤식으로 당겨주지? pop으로 뽑는다면 yx반전시키는방법도 있긴한데 
        # 
        return True # 성공했을때 트루만 반환 




