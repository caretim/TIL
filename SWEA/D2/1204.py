# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

# 다음과 같은 수 분포가 있으면,

# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

# 최빈수는 8이 된다.

# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).


import sys


sys.stdin = open("input.txt", "r")

# 딕셔너리로 키 값쌍으로 구성하여 가장 높은 값을 가진 수를 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_number =input()
    n= list(map(int,input().split()))

    nums={}

    for num in n:
        if num in nums :
            nums[num]+= 1
        else :
            nums[num]= 1
    
   
    print(f'#{test_number} {max(nums,key=nums.get)}') # 딕셔너리에서 맥스값 뽑는 방법