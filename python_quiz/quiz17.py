# > 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# `**.upper()`, `.swapcase()` 사용 금지**
# > 

# ### Input

# ```
# banana
# ```

# ### Output
# ### 파이썬 활용

# 특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다.

# [https://docs.python.org/ko/3/library/functions.html#ord](https://docs.python.org/ko/3/library/functions.html#ord)


# ord('a') 
# # 97


# 해당 유니코드 숫자를 문자로 반환하는 함수는 `chr`이다. 

# [https://docs.python.org/ko/3/library/functions.html#chr](https://docs.python.org/ko/3/library/functions.html#chr)

# ```python

# # 'a'


# a = ord('a')

# print(a)

# char = chr(97)
# print (char)

# change = a - 32
# print(change)

# chars = chr(int(change))

# print (chars)
# #for문을 통해 입력되는 문자를 ord함수의 번호로 저장되게 만든 후 저장된 문자를 chr함수를 통해 다시 치환
# # 대문자와 소문자의 ord 값 차이는 32  출력되는 값에 32를 더해서 다시 변환시키기 





# word = 'ppap'
word = input()
for i in word:
    b= ord(i) -32
    
    print(chr(int(b)),end="")

