# > 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 해당 문자열에서 등장한 모든 
# 알파벳 개수를 구해서 출력하세요.

# input 
# banana

#  Output
# b 1
# a 3
# n 2



# for문을 통해서 인풋되는 문장의 키값을 배정하고 업데이트를 통해 키의 값을 더해주고나서 마지막에 출력?


#키워드를 어떻게 딕셔너리에 새로 넣어줄 수 있을까? def 함수정의를 통해 **kwargs 로 넣어줄 수 있으니 활용해보자



word=('caca')

di = {}

for i in word:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

for k, v in di.items():

    print(k,v)

# c= 'c' 
# char.update (c=+1)

# print (char)


# char.update (c=+1)

# print (char)




# def char(**kwargs):
#     print(kwargs)

# word = 'chamchi'
# a = {}
# b = {}
# c = {} 
# d = {}
# e = {}
# f = {}
# g = {}
# h= {}
# i1 = {}
# j = {}
# k = {}
# l ={}
# m = {}
# n= {}
# o = {}
# p = {}
# q = {}
# r= {}
# s ={}
# t={}
# u ={}
# v= {}
# w={}
# x ={}
# y= {}
# z ={}

# for i in word:
#     if i == 'a':
#        char
#     elif i =='b':
#         b+=1
#     elif i =='c': 
#         c+=1
#     elif i =='d':
#         d+=1
#     elif i =='e':
#         e+=1
#     elif i =='f': 
#         f+=1
#     elif i =='g':
#         g+=1
#     elif i =='h':
#         h+=1
#     elif i1 =='i':
#         i1+=1
#     elif i =='j':
#         j+=1
#     elif i =='k':
#         k+=1
#     elif i =='l':
#         l+=1
#     elif i =='m':
#         m+=1
#     elif i =='n':
#         n+=1
#     elif i =='o':
#         o+=1
#     elif i =='p':
#         p+=1
#     elif i =='q':
#         q+=1
#     elif i =='r':
#         r+=1
#     elif i =='s':
#         s+=1
#     elif i =='t':
#         t+=1
#     elif i =='u':
#         u+=1
#     elif i =='v':
#         v+=1
#     elif i =='w':
#         w+=1
#     elif i =='x':
#         x+=1
#     elif i =='y':
#         y+=1
#     elif i =='z':
#         z+=1





# char( a = 1)
