import sys
input=sys.stdin.readline

# n= int(input())

# foods = {}

# root = set() #최초 시작노드 

# for __ in range(n):
#     Robot_root = list(input().split())
#     print(Robot_root)
#     prev = None
#     for i in range(1,int(Robot_root[0])):
#         now_Food =str(i)+Robot_root[i] # depth값과 문자열 합치기
#         if i==1: #최초 루트노드 생성 
#             root.add(now_Food) 
#             if now_Food not in foods:#만일 같은 뎁스에 현재노드가 존재하지않는다면
#                 foods[now_Food]=[]
#             prev = now_Food # 현재 노드 prev 설정 
#             continue
#         if now_Food not in foods: # 현재 노드가 foods에 존재한다면 prev에 현재노드 저장
#             foods[now_Food]=[] 
#         foods[prev].append(now_Food)

# print(root)
# print(foods)


import sys
input=sys.stdin.readline

n= int(input())

foods = []

#root 위치 따로 저장 후 이동 값 , 
for __ in range(n):
    Robot_root = list(input().split())
    for i in range(1,int(Robot_root[0])):
        now_Food =str(i)+Robot_root[i] # depth값과 문자열 합치기


