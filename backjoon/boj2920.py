# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.


# music= []
# music=list(map(int,input().split()))

# for _ in range(1,5):
#     if music[0] + music[7] == 9:
#         if music[1] + music[6] == 9:
#             if music[2] + music[5] == 9:
#                 if music[3] + music[4] == 9:
#                     if music[0] == 1:
#                         print('ascending')
#                         break
#                     elif music[0]==8:
#                         print('descending')
#                         break
# print('mixed')


music= []
music=list(map(str,input().split()))

mn =''.join((music))

if mn == '12345678':
    print('ascending')
elif mn == '87654321':
    print('descending')
else:
    print('mixed')