
# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.

# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.


num = int(input())

num_list = list(map(int,input().split())) #map은 리스트가 아님... 리스트로 뽑으려면 리스트로 정의해주자

list.sort(num_list)


mid = int(num /2)

# print 
# num_list.sort()

print (num_list[mid])