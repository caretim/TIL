# 백준 문제 풀이에 힘들어하는 수진이를 위해 민우는 문제해결에 도움이 되는 고무오리를 준비했다. 민우가 준비한 고무오리는 신비한 능력이 존재하는데, 최근에 풀던 백준 문제를 해결해주는 능력이다. 신비한 고무오리와 함께 수진이의 백준 풀이를 도와주자!

# 고무오리의 사용법은 다음과 같다.

# "고무오리 디버깅 시작" 이라고 외친다
# 문제들을 풀기 시작한다
# 고무오리를 받으면 최근 풀던 문제를 해결한다
# "고무오리 디버깅 끝" 이라고 외치면 문제풀이를 종료한다.
# 하지만 고무오리에는 치명적인 문제가 있는데, 풀 문제가 없는데 사용한다면 고무오리는 벌칙으 로 두 문제를 추가한다는 점이다.



from collections import deque


starting= input()

a= deque()

if starting == '고무오리 디버깅 시작':
    while True:
        word = input()
        if len(a)== 0 and word == '고무오리':
            a.append('문제')
            a.append('문제')
        elif word =='고무오리':
            a.popleft()            
        elif word =='문제':
            a.append('문제')
        elif word == '고무오리 디버깅 끝':
            break

if len (a) == 0: 
    print('고무오리야 사랑해')
else:
    print('힝구')