N = int(input())  # 도시의 수
M = int(input())  # 여행계획 도시의 수

graph = [[] for __ in range(N)]

for i in range(N):
    bridge = list(map(int, input().split()))
    for j in range(N):
        if bridge[j] == 1:
            graph[i].append(j)
            graph[j].append(i)

trips = list(map(int, input().split()))

result = "Yes"


def bfs(t, next):
    check_arr = [0] * (N + 1)
    check_arr[t] = 1
    q = []
    check = False
    q.append(t)
    while q:
        now_city = q.pop()
        for next_city in graph[now_city]:
            if check_arr[next_city] == 0:
                if next_city == next:
                    check = True
                    return check
                check_arr[next_city] = 1
                q.append(next_city)
    return check


for t in range(len(trips), 1, -1):
    if bfs(trips[t], trips[t - 1]) == False:
        result = "No"
        break

print(result)
