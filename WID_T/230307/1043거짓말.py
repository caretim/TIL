import sys

input= sys.stdin.readline

n,m= map(int,input().split()) # 사람 수 , 파티 수

#진실을 아는 사람과 같은 파티에 있게 된다면 파티의 사람들은 모두 진실을 알게된다.
#진실을 알게되는 사람들을 모두 체크 
# 진실을 모르는 사람들만 있을 때, 거짓말 가능 

# 놓친점 -> 파티는 순차적으로 진행되는게 아님, 
# 각 피플노드에 연결되는 파티리스트 정렬  노드-> 
# 각 
party = [1]*(m)  # 각각의 파티 

P=[0]*(n+1) # 진실을 아는 사람들 체크 

know= [[] for __ in range(n+1)] # 사람마다 가는 파티 어딘지 체크 



true_people =list(map(int,input().split())) # 진실을 아는 사람들 


if true_people[0]>0:
    for p in range(1,(true_people[0])+1):
        P[(true_people[p])]=1

party_room = [list(map(int,input().split())) for __ in range(m)]

for p in range(len(party_room)): # 사람들 파티 분류하기,
    j = party_room[p]
    pl=j[0]
    for i in j[1:]:
        know[i].append(p)
    

def dfs(true_people): # 진실을 아는 사람들 추가하기
    stack = true_people[1:]
    while stack:
        s = stack.pop()
        for k in know[s]: # 어디 파티가는지 확인 후 그 파티인원 모두 스택에 추가,
            party[k]=0
            k= party_room[k]
            for p in k[1:]: # 파티인원들이 어디 파티에 가는지 확인후 스택 추가, 
               if P[p]==0:
                   stack.append(p)
                   P[p]=1


# for y in range(len(party_room)):
#     room = party_room[y]
#     for x in range(1,room[0]+1):
#         member = room[x]
#         if P[member]==1:
#             party[y]=0
#             break

dfs(true_people)

print(sum(party))
