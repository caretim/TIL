# 영학이는 딸기우유, 초코우유, 바나나우유를 좋아한다.

# 입맛이 매우 까다로운 영학이는 자신만의 우유를 마시는 규칙이 있다.

# 맨 처음에는 딸기우유를 한 팩 마신다.
# 딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
# 초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
# 바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다. 
# 영학이는 우유 축제가 열리고 있는 우유거리에 왔다. 우유 거리에는 우유 가게들이 일렬로 늘어서 있다.

# 영학이는 우유 거리의 시작부터 끝까지 걸으면서 우유를 사먹고자 한다.

# 각각의 우유 가게는 딸기, 초코, 바나나 중 한 종류의 우유만을 취급한다.

# 각각의 우유 가게 앞에서, 영학이는 우유를 사마시거나, 사마시지 않는다.

# 우유거리에는 사람이 많기 때문에 한 번 지나친 우유 가게에는 다시 갈 수 없다.


n =int (input())

milks= list(input().split())


yd =[]
dri=0



for i in range(n):
    if  milks[i] == '1':
        if len(yd)== 1:
            dri +=1
            yd.append(milks[i])
    elif milks[i] == '2':
        if len(yd)== 2:
            dri +=1
            yd.append(milks[i])
    elif milks[i] == '0' :
        if len(yd) == 0:
            dri+=1
            yd.append(milks[i])  
        elif len(yd) == 3:
            yd =[]
            dri+=1
            yd.append(milks[i]) 


print(dri)



# n =int (input())

# milks= list(map(int,input().split()))


# dri=0

# for i in range(1,n):
#     if milks[i]==0:
#         if milks[i-1] !=0:
#             dri+=1
#         # elif milks[i-1]== 2:
#         #     dri+=1
#     elif milks[i]==1:
#         if milks[i-1]==0: 
#             dri+=1
#     elif milks[i]==2:
#         if milks[i-1]==1:
#             dri+=1
# if milks[0] == 0: 
#     dri+=1
# print(dri)
#     # print('.막')
# # if milks[n-1]== 0:
# #     if milks[n-2]==2:
# #         dri+=1
# #     print('막')



# # drinking =0

# # count= 0
# # for __ in range(idx):
# #     if len(milks_deq)>= 1 and milks_deq[0] == 0:
# #         milks_deq.popleft()
# #         if len(milks_deq)>= 1 and milks_deq[0]==0:
# #             pass
# #         else:
# #             drinking+=1
# #         if len(milks_deq)>= 1 and milks_deq[0] == 1:
# #             milks_deq.popleft()
# #             drinking+=1
# #             if len(milks_deq)>= 1 and milks_deq[0] == 2:
# #                 milks_deq.popleft()
# #                 drinking+=1
# #     elif len(milks_deq)== 0:
# #         print(drinking)
# #         break
# #     else :
# #         print(0)




# # idx =int (input())

# # milks= list(map(int,input().split()))



# # # count =0
# # # mlik = 0
# # # for i in range(n):
# # #     if milks[i] == 0 and milks[i+1] ==1:

