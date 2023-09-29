n,m= map(int,input().split())


trees = [[] for __ in range(n+1)]


def nodeRange(start,end):
   visit=[0]*(n+1)
   q=[]
   q.append((start,0))
   visit[0]=1
   while q:
       node,w = q.pop()
       if node == end:
           print(w)
           break
       for next_node,wei  in trees[node]:
           nextWei = w+wei
           if visit[next_node] == 0:
               q.append((next_node,nextWei))
               visit[next_node]=1
               



for __ in range(n-1):
    u,v,w = map(int,input().split())
    trees[u].append((v,w))
    trees[v].append((u,w))

for __ in range(m):
    start,end = map(int,input().split())
    nodeRange(start,end)

