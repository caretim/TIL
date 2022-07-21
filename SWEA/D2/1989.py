

#슬라이싱 사용방법

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = input()

    chars=[]
    for i in range(len(n)):
        i +=1
        chars.append(n[-i])

    r= ''.join(chars)


    if r == n:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')


 #문자열 슬라이싱 -1 방법
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n = input()
#     if n == n[::-1]:
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')
