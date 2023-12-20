n = int(input())

rock = list(map(int, input().split()))

start = int(input())

visited = [0] * (n)


def dfs(start):
    stack = []
    visited[start - 1] = 1
    stack.append(start - 1)
    cnt = 1
    while stack:
        node = stack.pop()
        for next_node in (node + rock[node], node - rock[node]):
            if 0 <= next_node < n and visited[next_node] == 0:
                cnt += 1
                visited[next_node] = 1
                stack.append(next_node)
    return cnt


print(dfs(start))
