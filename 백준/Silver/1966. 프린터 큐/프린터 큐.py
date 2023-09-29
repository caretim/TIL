import sys, heapq

t = int(sys.stdin.readline())
for i in range(t):
	n, m = map(int, sys.stdin.readline().split())
	idx_list = list(enumerate((map(int, sys.stdin.readline().split())))) # 최초 index 정보 저장을 위해 튜플 형태로 입력
	hq = [] # 문서의 중요도를 우선순위에 따라 배치하기 위해 heqpq 배열로 정보 재저장
	for j in range(n):
		heapq.heappush(hq, -idx_list[j][1]) # max_heap 구조를 위해 - 연산 후 저장
	cnt = 0
	while cnt <= n:
		if idx_list[0][1] == -hq[0] and idx_list[0][0] == m: # 현재 배열 첫번째 문서의 중요도와 우선순위 배열의 첫번째 중요도(가장 우선순위가 높은 것)와 같고, 그 문서의 인덱스가 처음 찾으려는 인덱스와 같을 경우 
			cnt += 1 # 카운트 증가 후 while문 중단
			break
		elif idx_list[0][1] == -hq[0]: # 현재 배열 첫번재 문서의 중요도와 우선순위 배열의 첫번째 중요도(가장 우선순위가 높은 것)와 같을 경우
			del idx_list[0] # 문서 삭제 == 출력
			heapq.heappop(hq) # 중요도 삭제 == 출력
			cnt += 1 # 출력 카운트 증가
		else: # 우선순위가 낮은 문서가 가장 첫번째에 잇을 경우
			idx_list.append(idx_list[0]) # 첫번째 문서를 뒤로 돌림
			del idx_list[0]
	print(cnt)