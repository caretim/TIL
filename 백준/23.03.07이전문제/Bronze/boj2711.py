# 창영은 맨날 오타를 낸다. 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 오타를 지운 문자열을 출력하는 프로그램을 작성하시오.

# 창영이는 오타를 반드시 1개만 낸다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1<=T<=1,000)가 주어진다. 각 테스트 케이스는 한 줄로 구성되어 있다. 첫 숫자는 창영이가 오타를 낸 위치이고, 두 번째 문자열은 창영이가 친 문자열이다. 문자열의 가장 첫 문자는 1번째 문자이고, 문자열의 길이는 80을 넘지 않고, 대문자로만 이루어져 있다. 오타를 낸 위치는 문자열 길이보다 작거나 같다.

T=int(input())

for time_case in range(T):

    chars=[]
    n,char= input().split()
    n_int =int(n)

    for i in range(len(char)):
        chars.append(char[i])

    chars.pop(n_int-1)

    print(''.join(chars))
    # for reselt in chars:
    #     print(reselt,end='')
