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
q2 = []
q1.append(1)
if check.popleft() != 1:
    print(0)
    exit()
result = 1  # 답 1 설정,
visit = [0] * (n + 1)
visit[1] = 1
while True:
    count = 0
    if result == 0:
        break
    check_list = []
    if len(q1) == 0:
        break
    q = q1.popleft()
    for i in arr[q]:
        if visit[i] == 0:
            q2.append(i)
            visit[i] = 1
            c = check.popleft()
            check_list.append(c)
            count += 1
    q2.sort()  # 방문리스트 둘 다 정렬 후 각각 비교 , 갯수가 틀리거나 수가 다르다면
    check_list.sort()
    for ii in range(count):
        try:
            q2[ii] == check_list[ii]
        except:
            result = 0  # 값이 틀렸을때
            break
    q1 = deque(q2)
    q2 = []

print(result)
