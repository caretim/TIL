import sys
from collections import deque

T = int(sys.stdin.readline()) # 테스트케이스 개수

for _ in range(T):
    p = sys.stdin.readline().rstrip() # 수행할 함수
    n = int(sys.stdin.readline()) # 배열에 들어있는 수의 개수

    # 배열 ([1,2,3,4]를 입력으로 받은 것을 리스트에 1, 2, 3, 4로 저장하기)
    arr = list(sys.stdin.readline().rstrip().split(','))
    arr[0] = arr[0][1:]
    arr[n-1] = arr[n-1][:len(arr[n-1])-1]

    # 리스트 형식의 arr을 덱 형식으로 변경
    arr = deque(arr)

    r = 1 # 뒤집기 여부 (r=1이면 앞부터, r=-1이면 뒤부터)
    error = 0 # error 발생 여부

    # p 하나씩 수행
    for fun in p:
        if fun == 'R':
            r = -r # r=1이면 앞부터(popleft), r=-1이면 뒤부터(pop)
        elif fun == 'D':
            # 배열이 비어있을때 D를 사용하면 에러
            if len(arr) == 0 or arr[0] == '':
                error = 1
                break

            # r=1이면 앞부터(popleft), r=-1이면 뒤부터(pop)
            if r == 1:
                arr.popleft()
            else:
                arr.pop()

    # r = -1이면 뒤집어서 출력
    if r == -1:
        arr.reverse()
    
    if error == 1: # error 발생했으면 error 출력
        print('error')
    else: # 리스트 형식으로 출력 ex)[1,2]
        print('[', end='')
        print(*arr, sep=',', end=']\n')