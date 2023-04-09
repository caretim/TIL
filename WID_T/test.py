from collections import deque

n = int(input())

arr = [[] for __ in range(n + 1)]

for __ in range(n - 1):
    u, v = map(int, input().split())
    arr[v].append(u)
    arr[u].append(v)
# 큐 나오는 순서 생각하기,

check = list(map(int, input().split()))
check = deque(check)
q1 = []

if check.popleft() != 1: # 맨처음 시작점 1부터 확인 후 q1d에 1 넣어준다.
    print(0)
    exit()
result = 1  # 답 1 설정,
visit = [0] * (n + 1) # 방문리스트 설정, 
visit[1] = 1 # 최초 1시작이며 방문체크, 

for __ in range(len(arr[1])):
    c =check.popleft()
    visit[c]=1
    q1.append(c)
k1= sorted(arr[1]) # 동일성 검사 ,
k2= sorted(q1)
if k1 != k2:
    print(0)
    exit()

def same(q1): # bfs로 다음번에 들어갈 리스트 번호 체크, 
    q= deque(q1)
    global visit
    check_list = []
    while q:
        x = q.popleft()
        for i in arr[x]:
            if visit[i] == 0:
                check_list.append(i)
                visit[i] = 1
    return check_list


while check: 
    check_list1 = same(q1)
    check_list2 =[]
    if len(check_list1)==0:
        break
    for __ in range(len(check_list1)): 
        check_list2.append(check.popleft())
        
    if sorted(check_list1) != sorted(check_list1): #bfs를 통해 가져온 리스트와 check에서 뽑아낸 리스트가 같은수인지 확인,
        result=0
        break
    else:
        q1 = check_list1

print(result)


# from collections import deque, defaultdict

# def bfs():
#     visited = [False] * (N+1)
#     queue = deque()
#     queue.append(1)
#     visited[1] = True

#     idx = 1
#     while queue:
#         x = queue.popleft()
#         children = []

#         for child in GRAPH[x]:
#             if not visited[child]:
#                 visited[child] = True
#                 children.append(child)

#         if sorted(answer[idx:idx+len(children)]) == sorted(children):
#             for child in answer[idx:idx+len(children)]:
#                 queue.append(child)
#             idx +=len(children)
#         else:
#             return 0
              
#     return 1

# GRAPH = defaultdict(list)

# N = int(input())
# for _ in range(N-1):
#     start, end = map(int, input().split())
#     GRAPH[start].append(end)
#     GRAPH[end].append(start)

# answer = list(map(int, input().split()))

# if answer[0] == 1:
#     print(bfs())
# else:
#     print(0)





# from collections import deque

# n = int(input())

# arr = [[] for __ in range(n + 1)]

# for __ in range(n - 1):
#     u, v = map(int, input().split())
#     arr[v].append(u)
#     arr[u].append(v)
# # 큐 나오는 순서 생각하기,

# check = list(map(int, input().split()))
# check = deque(check)
# q1 = deque()
# q2 = []
# q1.append(1)
# if check.popleft() != 1:
#     print(0)
#     exit()
# result = 1  # 답 1 설정,
# visit = [0] * (n + 1)
# visit[1] = 1
# while True:
#     count = 0
#     if result == 0:
#         break
#     check_list = []
#     if len(q1) == 0:
#         break
#     q = q1.popleft()
#     for i in arr[q]:
#         if visit[i] == 0:
#             q2.append(i)
#             visit[i] = 1
#             c = check.popleft()
#             check_list.append(c)
#             count += 1
#     q2.sort()  # 방문리스트 둘 다 정렬 후 각각 비교 , 갯수가 틀리거나 수가 다르다면
#     check_list.sort()
#     for ii in range(count):
#         try:
#             q2[ii] == check_list[ii]
#         except:
#             result = 0  # 값이 틀렸을때
#             break
#     q1 = deque(q2)
#     q2 = []

# print(result)