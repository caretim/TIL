# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.

'b''d''p''q'
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    char= input()

    rechar=[]

    for i in char:
        if i =='b':
            i= i.replace('b','d')
            rechar.append(i)
        elif i =='d':
            i= i.replace('d','b')
            rechar.append(i)
        elif i == 'p':
            i= i.replace('p','q')
            rechar.append(i)
        elif i == 'q':
            i= i.replace('q','p')
            rechar.append(i)

    reselt= ''.join(rechar)[::-1]
    
    print(f'#{test_case} {reselt}')
