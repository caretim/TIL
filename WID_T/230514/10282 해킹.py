import sys
import heapq


INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(virus):
    computers = [INF] * (n + 1)
    computers[virus] = 0
    result = 0
    count = 0
    q = []
    heapq.heappush(q, (0, virus))
    while q:
        time, computer = heapq.heappop(q)
        if computers[computer] < time:
            continue
        for add_time, next_computer in graph[computer]:
            cost_time = time + add_time
            if computers[next_computer] > cost_time:
                computers[next_computer] = cost_time
                heapq.heappush(q, (cost_time, next_computer))
    for i in computers:
        if i != INF:
            count += 1
            if result < i:
                result = i
    return count, result


for test_case in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for __ in range(n + 1)]
    for __ in range(d):
        u, v, w = map(int, input().split())
        graph[v].append((w, u))

    print(*dijkstra(c))
