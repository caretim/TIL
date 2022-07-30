
# 직사각형의 네 변 중에서 세 변의 길이가 주어진다.

# 나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.

# 세 변의 길이는 상하좌우 어디든 될 수 있으므로 그 순서는 중요하지 않다.

# 입력으로 직사각형이 불가능한 경우는 주어지지 않는다.


# 다음 그림의 예시는 각각 a = 4, b = 3, c = 4의 입력과 a = 5, b = 5, c = 5의 입력을 받았을 때 직사각형의 모습이다.

# 빨간 숫자로 표시된 나머지 변의 길이를 출력하면 된다.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num =[]
    num=list(map(int,input().split()))


    if num[0] == [num[1]] and num[1] ==num[3]:
        print(f'#{test_case} {num[0]}')
    elif num[0] == num[1]:
        print(f'#{test_case} {num[2]}')
    elif num[1] == num[2]:
        print (f'#{test_case} {num[0]}')
    elif num [2] == num[0]:
        print (f'#{test_case} {num[1]}')