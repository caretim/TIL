# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# input = apple  , output= 1
#test case = banana # 3 ,kiwi # 0


word = input()
a = 'a'
r= 0

for i in word:
    if a in i :
        r += 1
    

print(r)