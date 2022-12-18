from collections import deque


def bfs(y, x):  # 지점 간 1000의 거리 내로 이동이 가능한가 bfs탐색 시작  
    q = deque()  # bfs탐색을 위해 큐로 넣어준다.
    q.append((y, x))
    while q:  
        k = q.popleft()
        if (abs(k[0] - festivaly) + abs(k[1] - festivalx) <= 1000):  # 큐에서 뽑힌 값이 락페스티벌 장소로 갈 떄 1000이하로 도착할 수 있는지 확인
            return print("happy")  # 도착할 수 있다면 happy 출력
        for index in con:  # 모든 편의점 리스트를 for문을 통해 꺼내온다. con = 리스트에 담긴 편의점의 좌표 ,  # bfs   -음수 <=     = >  양수 
            conyx = abs(k[0] - index[0]) + abs(k[1] - index[1])    # k = 시작지점과, 1000의 거리에서 갈 수있는 값이 들어간 큐에서 뺴낸 위치 값 ,# 큐에 추가된 장소에서 남은 편의점들을 갈 수 있는지 확인, 갈 수 있다면 큐에 추가
            if conyx <= 1000:                           # 델타탐색은 사방을 탐색하고, 이문제는 1000내로 갈 수 있는 위치 확인해서 큐에 넣어주는 방식  
                q.append((index[0], index[1]))  # 큐에 넣어준 후  ,
                con.remove((index[0], index[1]))   # 방문했던 편의점을 remove로 삭제, (remove(value,value))를 통해 튜플로 묶인 리스트값 삭제 가능
    return print("sad") # 처음 위치에서 갈 수 있는 모든 편의점을 다 들렀을 떄 락페스티벌 장소를 못갔다면 sad를 출력, (q의 인자가 0이 됬을 때)

for test_case in range(int(input())):    # 시작점 - > 편의점 -> 락페스티벌  [맨하탄] 현재위치 [x,y] 목적지[x,y]  (현재위치 x 목적지 x)   (현재위치 y 목적지 y)  
   
    shop = int(input())   #편의점의 갯수 

    start_y, start_x = map(int, input().split()) # 시작지점 설정  시작지점 yx 

    con = deque()  # 굳이 큐를 사용 안해도됨 ㅎㅎ,,,
    con = []            # 받는 편의점의 좌표값, 그리고 마지막값  n의 개수만 넣어줘도되는데 

    for __ in range(shop + 1): # 편의점 위치 추가 , 마지막 값은 락페스티벌의 위치
        y, x = map(int, input().split())
        con.append((y, x))

    end = con.pop()
 
    festivaly = end[0]  #  락페스티벌 위치 지정   

    festivalx = end[1] 


    bfs(start_y, start_x)  # 시작지점을 bfs로 탐색시작 

# 간단하게 연산으로만 풀기,


# n = int(input())

# yard = []

# bw = 1000
# 1
# for __ in range(n + 2):
#     y, x = map(int, input().split())
#     yard.append(y + x)

# now = yard[0]

# 0 - 1000

# finish = yard[n + 1]  # 인덱스 시작 0
# for i in range(1, n + 2):
#     if now - yard[i] >= -1000:  # 400 1300
#         print("sad")
#     elif now - yard[i] <= -1000:
#         now = yard[i]
#         pass
# print("happy")