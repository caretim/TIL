#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.


# 인풋 값에서 for문을 사용해서 if문을 통해 동일한 문자가 감지되면 지우는 방법

# word = ['apple']

# b= 'a'

# for a in word:
#     if a == 'a':
#         word.remove('a')
#         print(a)
        
# print(word)

# word.remve()로는 인풋값을 잡지못한다. 그래서 replace를 사용해봄
# from dataclasses import replace


# word = input()


# for char in word:
#     if char == 'a':
#        b= word.replace('a',' ')
        
     
        
# print(b)



#continue를 사용하는 방법


word = input()


for char in word:
    if char == 'a':
        continue
    print(char,end="")