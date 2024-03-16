# import sys
# input =sys.stdin.readline
# # sys.stdin = open("input.txt", "r")

# # 8퍼에서 틀리는 이유 
# def find(node):
#     if root[node] ==node:
#         return node
#     else:
#         while root[node]!=node:
#             node= root[node]
#             root[node] = root[root[node]]
#         return node

# def union(x,y):
#     a= find(x)
#     b= find(y)
#     if a < b:
#         root[b] = root[a]
#     elif a > b:
#         root[a] = root[b]
#     else:
#         cycle.add(a)


    
# tc= 0
# while True:
#     tc+=1

#     n,m= map(int, sys.stdin.readline().split())
#     if n ==0 and m == 0:
#         break

#     root = [i for i in range(n)]


#     cycle =set()

#     for __ in range(m):
#         a,b = map(int, sys.stdin.readline().split())
#         union(a-1,b-1)

#     for i in range(n):
#         find(i)

#     root = set(root)

#     for i in cycle:
#         root.discard(i)
    




#     if len(root)==0:
#         print(f'Case {tc}: No trees.')
#     elif len(root) == 1:
#         print(f'Case {tc}: There is one tree.')
#     else:
#         print(f'Case {tc}: A forest of {len(root)} trees.')

    




def get_parent(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = get_parent(parent[idx])
    return parent[idx]

def find_union(x1, x2):
    idx1 = get_parent(x1)
    idx2 = get_parent(x2)
    if idx1 > idx2:
        parent[idx1] = idx2
    elif idx1 < idx2:
        parent[idx2] = idx1
    else:
        parent[idx1] = 0
        parent[idx2] = 0
import sys
input = sys.stdin.readline
num = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    parent = [i for i in range(n+1)]

    for _ in range(m):
        x1, x2 = map(int, input().split())
        find_union(x1, x2)
        
    count = set()
    for i in range(1, n+1):
        p = get_parent(parent[i])
        if p and p not in count:
            count.add(parent[i])

    case = f'Case {num}'
    if len(count) == 0:
        print(f'{case}: No trees.')
    elif len(count) == 1:
        print(f'{case}: There is one tree.')
    else:
        print(f'{case}: A forest of {len(count)} trees.')
    num += 1