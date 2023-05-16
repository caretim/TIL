import heapq

# Dijkstra's 알고리즘을 사용하여 최단 경로를 찾는 함수
def dijkstra(grid, start):
    h = len(grid)
    w = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # 시작 위치에서 각 셀까지의 최단 경로 거리를 저장할 배열
    distances = [[float("inf")] * w for _ in range(h)]
    distances[start[0]][start[1]] = 0

    # 우선순위 큐를 사용하여 다음에 방문할 셀을 관리
    queue = [(0, start)]

    while queue:
        curr_dist, curr_pos = heapq.heappop(queue)

        # 현재 셀의 최단 경로 거리보다 큰 경우 무시
        if curr_dist > distances[curr_pos[0]][curr_pos[1]]:
            continue

        for direction in directions:
            new_x = curr_pos[0] + direction[0]
            new_y = curr_pos[1] + direction[1]

            # 맵을 벗어나는 경우 무시
            if new_x < 0 or new_x >= h or new_y < 0 or new_y >= w:
                continue

            # 높이 차이 계산
            if grid[new_x][new_y] == "#":
                continue
            diff = abs(int(grid[curr_pos[0]][curr_pos[1]]) - int(grid[new_x][new_y]))

            # 에너지 계산
            energy = 1 if diff == 0 else (diff + 1) ** 2

            # 새로운 셀로 이동하는 경우 최단 경로를 업데이트하고 우선순위 큐에 추가
            if curr_dist + energy < distances[new_x][new_y]:
                distances[new_x][new_y] = curr_dist + energy
                heapq.heappush(queue, (curr_dist + energy, (new_x, new_y)))

    return distances


# 테스트 케이스 개수 입력
T = int(input())

for _ in range(T):
    # 지도 크기 입력
    h, w = map(int, input().split())

    # 지도 정보 입력
    grid = [input().strip() for _ in range(h)]

    # 시작 위치 입력
    start = tuple(map(int, input().split()))

    # 시작 위치에서 가장 높은 셀까지의 최단 경로 계산
    distances = dijkstra(grid, start)

    # 가장 높은 셀의 최단 경로 출력
    highest_cell = max(max(distances, key=max))
    if highest_cell == float("inf"):
        print("NO")
    else:
        print(highest_cell)
