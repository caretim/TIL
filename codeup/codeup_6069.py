# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

char = input()
a = 'A'
b = 'B'
c = 'C'
d = 'D'



if char == a :
    print ('best!!!')
elif char == b:
    print ('good!!')
elif char == c:
    print('run!')
elif char == d:
    print('slowly~')
else :
    print('what?')