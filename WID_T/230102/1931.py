# -*- coding: utf-8 -*-

# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.


import heapq,sys
input= sys.stdin.readline

n= int(input())

time_list = []

for __ in range(n):
    start,end = map(int,input().split())
    heapq.heappush(time_list,(end,start))
   

result =[]

end_time = 0
for k in range(len(time_list)):
    a= heapq.heappop(time_list)
    if end_time<=a[1]:
        result.append(a)
        end_time=a[0]


print(len(result))