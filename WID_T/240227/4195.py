# #백준 https://www.acmicpc.net/problem/4195



# import sys
# input =sys.stdin.readline


# tc = int(input())

# for __ in range(tc):
#     n =int(input())

#     relationship = {}

#     root ={}
#     #친구 전체 관계네트워크의 수를 알려줘야함 ,

#     def find_root(node): # 재귀적으로 root노드 찾기
#         if root[node]!= node:
#             return find_root(root[node])
#         return node
            
#     def union(a,b):
#         ra = find_root(a)
#         rb= find_root(b)

#         if ra<rb:
#             root[b] =ra
#             relationship[ra] = relationship[ra]|relationship[rb]
#             return ra
#         else:
#             root[a] =rb
#             relationship[rb] = relationship[ra]|relationship[rb]
#             return rb
        

#     for __ in range(n):
#         a,b =input().split()
#         if a not in root:
#             root[a]=a
#             relationship[a] = set()
#             relationship[a].add(a)

#         if b not in root:
#             root[b]=b
#             relationship[b] =set()
#             relationship[b].add(b)

#         r = union(a,b)
#         # if r not in relationship:
#         #     relationship[r] = set()
#         # relationship[r] = relationship[r]| relationship[a] | relationship[b]
#         print(len(relationship[r]))




#     # print((relationship[a]|relationship[b]))


#백준 https://www.acmicpc.net/problem/4195



import sys
input =sys.stdin.readline
sys.setrecursionlimit(100001)
def find_root(node): # 재귀적으로 root노드 찾기
    if root[node]!= node:
        return find_root(root[node])
    return node
        
def union(a,b):
    ra = find_root(a)
    rb= find_root(b)

    if ra!=rb:
        root[b]=ra
        relationship[ra]+= relationship[rb]



tc = int(input())

for __ in range(tc):
    n =int(input())

    relationship = {}

    root ={}

    for __ in range(n):
        a,b =input().split()

        if a not in root:
            root[a]=a
            relationship[a] = 1
        if b not in root:
            root[b]=b
            relationship[b] = 1
        union(a,b)
        print(relationship[find_root(a)])







