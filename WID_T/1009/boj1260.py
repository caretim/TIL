n, m, v = map(int, input().split())


visit = [0] * (n + 1)  # 방문체크를 위한 방문리스트

graph = [[0] * (n + 1) for __ in range(n + 1)]  # 노드들의 행렬 (방향 표시)

for __ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1  # 입력 값을 받고 노드에 인접노드 표기 a-> b b <-a 방향을 0에서 1로 표시해줌


result1 = []  # dfs의 답이 적혀서 나갈 리스트
result2 = []  # bfs의 답이 적혀서 나갈 리스트


def dfs(v):

    visit[v] = 1  # 방문한곳 방문처리
    result1.append(v)  # 방문하게 된 노드를 dfs리스트 답에 추가해줌,

    for i in range(1, n + 1):  # 노드의 모든 범위를 for문으로 순회하며 1과 연결 될 수 있는 모든 노드 탐색
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):

    queue = [v]  # 큐에 v를 넣어줌
    visit[v] = 0  # 방문한곳 방문처리
    while len(queue) >= 1:  # 큐에 담긴 수가 0이된다면 1로 통하는 모든 노드 탐색 완료
        v = queue.pop(0)  # 큐에 담긴 첫번째 인자를 가져온 후 탐색
        result2.append(v)  # 탐색된 값은 출력리스트에 추가
        for i in range(1, n + 1):  # 탐색하게된 노드에 인접리스트 확인 1이라면 존재하는 노드
            if visit[i] == 1 and graph[v][i] == 1:  # 노드를 탐색하며 방문하지 않았고 인접노드가 존재한다면
                queue.append(i)  # 탐색해줄 큐리스트에 추가해줌
                visit[i] = 0  # 방문했음을 확인하기 위해 1을 0으로 변경해준다.


dfs(v)
bfs(v)

print(*result1)
print(*result2)
