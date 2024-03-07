import sys

input =sys.stdin.readline
def find(node):
    if root[node] ==node:
        return node
    else:
        while root[node]!=node:
            node= root[node]
            root[node] = root[root[node]]
        return node

def union(x, y):
    x, y = find(x), find(y)
    root[y] = x

num = 0
while True:
    n = int(input())
    if not n:
        break
    num += 1
    cache = dict()
    cnt = 0
    temp = []
    for _ in range(n):
        a, b = input().split()
        if a not in cache:
            cache[a] = cnt
            cnt += 1
        if b not in cache:
            cache[b] = cnt
            cnt += 1
        temp.append((a, b))
    root = [i for i in range(cnt)]
    ans = 0
    for i in temp:
        if find(cache[i[0]]) != find(cache[i[1]]):
            union(cache[i[0]], cache[i[1]])
        else:
            ans += 1
            union(cache[i[0]], cache[i[1]])
    print(num, ans)