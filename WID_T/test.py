
for a, b, c in permutations(mid, 3):
    total = dist[x][a] + dist[a][b] + dist[b][c] + dist[c][z]
    if result > total:
        result = total
if result == INF:
    result = -1
print(result)