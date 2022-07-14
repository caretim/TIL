# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지


word = input()

mo = ['a','e','i','o','u']

r = 0

for j in word:
    if j in mo: # ==같다와 in의 차이 생각해서 코드작성 개별하기
        r += 1 

print (r)


