import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline

while True:
    try:
        n,m= map(int,input().split())
        


        graph = [[] for __ in range(n+1)]

        for __ in range(m):
            u,v,w = map(int,input().split())
            graph[u].append((w,v))
            graph[v].append((w,u))


        def dijkstra(start):
            arr=[INF]*(n+1)
            q=[]
            arr[start]=100
            heapq.heappush(q,(-100,start))
            while q:
                w,node= heapq.heappop(q)
                if arr[node]<w:
                    continue
                for wei,next_node in graph[node]:
                    cost = w*wei/100
                    if arr[next_node]>cost:
                        arr[next_node] = cost
                        heapq.heappush(q,(cost,next_node))
            return arr

        r =dijkstra(1)
        result = -r[n]
        print("{:.6f} percent".format(result))
    except:
        break