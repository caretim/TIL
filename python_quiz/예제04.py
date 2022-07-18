# > 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# > 

# ### 오류 코드

# words = list(map(int, input().split()))
# print(words)

# ### Input

# I'm Tuotur 6

# ### Output
# ["I'm", 'Tutor', '6']


words =input().split()
print(words)
#    words = list(map(int, input().split()))
# ValueError: invalid literal for int() with base 10: 'im'
# 입력값이 int로 형변환 되어있어서 문자가 입력되지 못한다 int 제거
