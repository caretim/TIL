import sys,heapq
n= int(input())

PB=[]

for __ in range(n):
    #데드라인,라면 
    L,M = map(int,input().split())
    heapq.heappush(PB,(L,M))

result = []

#데드라인을 우선순위 큐로 돌리면서 라면의 보상이 가장 큰 순서로 리스트의 안의 값을 갱신
#1.데드라인 기준으로 데이터 정렬하기 - > 데이터를 우선순위 큐로 데드라인에서 가장 작은 값으로 꺼내온다,
#2.갱신되는 값은 라면이 가장 적은 튜플의 값을 갱신시켜야한다,
#3.result에 갱신되는 값은, 라면의 개수가 앞으로 오도록 한다
#4. result의 인자 개수는 day함수와 동일해야한다 - > day가 증가될 떄 , (0,day) 튜플 삽입,

PB.sort()
day = 0
cnt_min = 1e9
while PB:
    t,m = heapq.heappop(PB)
    #데드라인 시간이 변경될 경우  result에 들어갈 공간 추가 
    if t!=day:
        day+=1
        heapq.heappush(result,m)
        continue
    if m>result[0]:
        heapq.heappop(result)
        heapq.heappush(result,m)

print(sum(result))



    
