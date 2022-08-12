
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = map(int,input().split( ))

    cnt= 0
    for i in n:
        if i%2 != 0:
            cnt += i

    print(f'#{test_case} {cnt}')


