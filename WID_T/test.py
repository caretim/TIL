import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline


def find(v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        a, b = b, a

    parent[b] = a
    if not a == b:
        network[a] += network[b]


T = int(input())

for _ in range(T):
    F = int(input())

    friends = {}
    parent = []
    network = []
    cnt = 0
    for _ in range(F):
        f1, f2 = input().split()
        if f1 not in friends:
            friends[f1] = cnt
            parent.append(cnt)
            network.append(1)
            cnt += 1
        if f2 not in friends:
            friends[f2] = cnt
            parent.append(cnt)
            network.append(1)
            cnt += 1
        union(friends[f1], friends[f2])
        print(network[find(friends[f1])])
