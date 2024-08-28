import sys,heapq


input = sys.stdin.readline

n= int(input())

# 비교순서  1. 순서  2. 높이 - 시작과 끝이 어떻게 되는지, 

# 그냥 순서대로 나오고 나오는 데이터가 끝나는 순서를 prev에 저장해주기,

# prev가 마지막 순서보다 적다면 앞데이터 끝부분을 0으로 기록 ,


# if 분기를 통해 처리하기 

# 0부터 시작해서 1 ~ 6     4~ 8 일경우

# 1시작 6마무리 

# 시작과 끝 결정 - > 입력되는 데이터를 기준으로 시작과 끝을 구분해준다,


result=[]

heap = []
endList = []
for i in range(n):
    x,h,y = map(int,input().split())
    heapq.heappush(heap,(x,h,1,i)) # 시작
    heapq.heappush(heap,(y,h,0,i)) # 종료 
    endList.append((y))
#시작과 끝을 기준으로 데이터 갱신 및 출력해주기 

#현재
now =(0,0,0,-1)

prev=(0,0,0,-1)


#종료지점끼리만 비교해주는게 제일 효과적이지 않나?
while heap:
    ny,nh,al,i = now = heapq.heappop(heap)
    if al: # 시작점 일떄
        if nh > now[1]: 
            if endList[now[3]] > endList[i]:# 현재 데이터의 위치 길이가 새로운 데이터보다 늦게 종료된다면 prev로 저장
                prev = now
            now = (ny,nh,al,i) # now값 갱신 ,
        else: # 이미 작은값, 
            nh 
    else: # 종료점 일떄
        if ny>now[0]:# 종료점이 현재의 마지막 부분보다 뒤쪽일 경우
            print(now[0])









