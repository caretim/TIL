n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

matrix = [list(map(int, input().split())) for __ in range(m)]


cnt = 0
year =0


while cnt > 1:
    year+=1 
    bingsan = 0
    for y in range(n):
        for x in range(m):
            if matrix [y][x]>=1:
                bingsan+=1
        
        if bingsan > 1:
            print(year)
        elif bingsan == 0:
            print ('0')
    



    

#     def 한번 실행할떄 높이 -1씩  

#     깍고나서 빙산쪼개졌는지 안쪼개졌는지 확인 ,

#     for y in range(m):
#         for x in range(n):
            
#             각각의 매트릭스 
            
#              빙산들 안의 높이를 한번 돌때 사방의 0의 숫자를 카운트해서 좌표값의 높이를 1씩 빼줌)

#             (-> 그리고 탐색했을때 각각 빙산들의 주변 사방을 델타탐색을 통해서 0의 숫자를 카운트하고 -> 높이를 줄여줍니다.

#             이걸 하면서 동시에, 방문처리 한번의 그래프 탐색을 할때 각각 방문위치를 기록해줘야함. ) 

# 해당 좌표의 상하좌우 빈공간바다 (0) 가 존재할 경우 매년 빙산의 길이가  -

# 4방위 델타탐색을 해야하는데, 먼저 저희가 구해야 할 부분은 , 빙산이 두개로 쪼개는 순간이 언제인지 확인을해야함,
#-> 빙산  두개 쪼개지는것 , 그리고 시간이 흐르면서 빙산의 높이가 줄어드는것을 생각해야함, 