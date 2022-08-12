# #1분에 한 대당 A원을 내야 한다. 두 대를 주차할 때는 1분에 한 대당 B원, 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.

import pprint

cost1,cost2,cost3=map(int,input().split())


pl=[[0]*100 for __ in range(3)]


for car in range(3):
    c1,p1 = map(int,(input().split()))
    for m in range(c1,p1):
        pl[car][m]=1

cost =0
for x in range(100):
    car=0
    for y in range(3):
        car+=pl[y][x]
    
    if car == 0:
        pass
    elif car == 1:
        cost+= car*cost1
    elif car == 2:
        cost+= car*cost2
    elif car == 3:
        cost+= car*cost3
print(cost)






# #         car1.append(m)
# c1,p1 = map(int,(input()))
# c2,p2 = map(int,(input()))
# c3,p3 = map(int,(input()))



# car1= []
# car2= []
# car3= []


# for m in range(c1,p1+1):
#     car1.append(m)
# for m in range(c2,p2+1):
#     car2.append(m)
# for m in range(c3,p3+1):
#     car3.append(m)




# cost1,cost2,cost3=5,3,1

