# i,l,m,a  # 암소,달리는시간,달리고나서 수행할 신호 수 , 다음차례의 암소
import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize


n = int(input())

runtime = [0] * (1001)

graph = [[] for __ in range(1001)]
check = [0] * (n + 1)

time_list = [0] * (n + 1)

for cow in range(1, n + 1):
    order = list(map(int, input().split()))
    runtime[cow] = order[0]
    try:
        k = order[2:]
        for i in range(len((k))):
            graph[cow].append(k[i])
    except:
        pass


q = []
heapq.heappush(q, (runtime[1], 1))
time_list[1] = runtime[1]
check[0] = 1
while q:
    time, cow = heapq.heappop(q)
    for next_cow in graph[cow]:
        if check[next_cow] == 0:
            time_list[next_cow] = time + runtime[next_cow]
            check[next_cow] = 1
            heapq.heappush(q, (time + runtime[next_cow], next_cow))

print(max(time_list))
