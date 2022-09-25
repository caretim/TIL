import sys

#카운팅 정렬(Counting Sort, 계수 정렬)이란?
# 주어진 배열의 값 범위가 작은 경우 빠른 속도를 갖는 정렬 알고리즘이다.
#  최댓값과 입력 배열의 원소 값 개수를 누적합으로 구성한 배열로 정렬을 수행한다.

# 카운팅 정렬 수행 과정

# 1.입력 배열의 최댓값,  최댓값 +1의 Counting Array 생성한다.

nls= [0]*10001  # 배열의 최댓값은 10000

# 2. 좌표의 원소를 더해 나가는 누적합 배열을 만들어준다.
    # 리스트의 인덱스 위치와 숫자를 체크한 후 리스트의 좌표에 입력값을 더 해준다.
n= int(sys.stdin.readline().rstrip())
for __ in range(n):
    nls[int(sys.stdin.readline().rstrip())]+=1
#ex) input list= [4,1,5,4,5] -> counting array = [[1],[0],[],[2],[2]]

# 
for i in range(10001):
    if nls[i]>=1 : # counting array의 인덱스중 1보다 이상인 값을  확인 한다. (0인 값은 입력을 못 받은 값)
        for __ in range(nls[i]):  # 인덱스이 값만큼 인덱스의 좌표 (인덱스번호)를 출력한다.
            print(i)
