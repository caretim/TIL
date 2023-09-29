import sys, heapq

input = sys.stdin.readline
t = int(input())

for i in range(t):
	

	n, m = map(int, input().split())


	l_list = list(enumerate((map(int,input())))) 

	heap = [] 
	for j in range(n):
		heapq.heappush(heap, -l_list[j][1]) 
	cnt = 0
	while cnt <= n:
		if l_list[0][1] == -heap[0] and l_list[0][0] == m: 
			cnt += 1 
			break
		elif l_list[0][1] == -heap[0]: 
			del l_list[0] 
			heapq.heappop(heap)
			cnt += 1
		else: 
			l_list.append(l_list[0]) 
			del l_list[0]
	print(cnt)