# 영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.

# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 글의 문장이 주어진다. 글은 최대 50개의 줄로 이루어져 있고, 각 줄은 최대 50개의 글자로 이루어져 있다. 각 줄에는 공백과 알파벳 소문자만 있다. 문장에 알파벳은 적어도 하나 이상 있다.

# 출력
# 첫째 줄에 가장 많이 나온 문자를 출력한다. 여러 개일 경우에는 알파벳 순으로 앞서는 것부터 모두 공백없이 출력한다.


import sys
sen =sys.stdin.read().replace('\n','')


ch ={}



for char in sen:
    if char == ' ': 
        pass
    elif char not in ch:
        ch[char]=1
    elif char in ch:
        ch[char]+=1

a = max(ch.values())

maxl=[]

for i in ch:
    if ch[i]== a :
        maxl.append(i)

maxl.sort()

print(*maxl,sep='')
print

# import sys

# # sen=sys.stdin.read()

# sen= input()

# char = [0]*26

# for ch in sen:
#     if ch == ' ':
#         pass
#     else:
#         char[ord(ch)-97]+=1

# maxc = max(char)

# for r in range(26):
#     if char[r]== maxc:
#         print(chr(97+r),end='')
