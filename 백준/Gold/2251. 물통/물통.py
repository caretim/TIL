import sys
A, B, C = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(B + 1)] for _ in range(A + 1)]

def dfs(a, b):
    if visited[a][b] == 0:
        visited[a][b] = 1
        c = C - a - b
        # A -> B
        if a + b < B: dfs(0, a + b)
        else: dfs(a + b - B, B)
        # A -> C
        if a + c < C: dfs(0, b)
        else: dfs(a + c - C, b)
        # B -> A
        if b + a < A: dfs(b + a, 0)
        else: dfs(A, b + a - A)
        # B -> C
        if b + c < C: dfs(a, 0)
        else: dfs(a, b + c - C)
        # C -> A
        if a + c < A: dfs(a + c, b)
        else: dfs(A, b)
        # C -> B
        if b + c < B: dfs(a, b + c)
        else: dfs(a, B)

dfs(0, 0)
ans = [C - i for i in range(B, -1, -1) if visited[0][i] == 1]
print(*ans)