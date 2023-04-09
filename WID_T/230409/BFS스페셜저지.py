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


# def find_num(q1,re):
#     global visit
#     global check
#     q = deque(q1)
#     q2=[]
#     result = re
#     while q:
#         if result == 0:
#             break
#         node = q.popleft()
#         for i in arr[node]:
#             if visit[i] == 0:
#                 if i == check.popleft():
#                     visit[i] = 1
#                     q.append(i)  # 순서확인을 어떻게?
#                 else:
#                     result = 0
#     return result


# q1 = deque()
# q2 = []
# if check.popleft() != 1:
#     print(0)
#     exit()
# result = 1  # 답 1 설정,
# visit = [0] * (n + 1)
# visit[1] = 1

# first_check1 = []
# first_check2 = []
# for __ in range(len(arr[1])):
#     f = check.popleft()
#     first_check1.append(f)
#     visit[f] = 1
# for cn in arr[1]:
#     first_check2.append(cn)

# if first_check1 == first_check2:
#     result = find_num(first_check1,1)  # 최초의 시작점 설정,
# else:
#     result = 0


# print(result)


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
q1 = deque()
q1.append(1)
if check.popleft() != 1: # 맨처음 시작점 1부터 확인 후 q1d에 1 넣어준다.
    print(0)
    exit()
result = 1  # 답 1 설정,
visit = [0] * (n + 1) # 방문리스트 설정, 
visit[1] = 1 # 최초 1시작이며 방문체크, 

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
    print(sorted(check_list),sorted(arr[1:len(check_list)]))
    if  sorted(check_list) == sorted(arr[1:len(check_list)]):
        check_list = arr[len(check_list):]
    else:
        check_list="fail"
    return check_list


while check:
    check_list1 = same(q1)
    if check_list1=="fail":
        result=0
        break
    # if len(check_list1)==0:
    check_list2 =[]
    for __ in range(len(check_list1)):
       check.popleft()
    q1 = check_list2

print(result)
    





# 먼저. 1에서 연결된 노드 2,3체크해서 팝, 순서대로 2,3 2번노드 숫자 빼서 체크, 3번노드 숫자빼서 체크, q 비었으면

# 체크한숫자들 q에 다시 넣어주기, 