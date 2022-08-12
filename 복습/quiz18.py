# > 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# > 

# ### Input

# ```
# banana
# ```

# # ### Output
# #b 1
# a 3
# # n 2





word = 'friedchicken'

dic = {}

for i in word:
    if i in dic:
        dic[i] +=1
    else :
        dic[i] = 1

print(dic)

for k,v in dic.items():
    print(k,v,sep=' ')



# word = 'banana'

# dit = {}

# for i in word: # i라는 변수로 word의 요소를 순환시킴
#     if i in dit: # i의 변수가 dit 딕셔너리에 있는지 없는지 확인 
#         dit[i] +=1  #딕셔너리에 i와 같은 값이 있다면 플러스 1
#     else:
#         dit[i] = 1 # 딕셔너리에 같은 값이 없다면 i : 1로 키와 값 쌍을 딕셔너리에 생성 

# print(dit)

# for k,v in dit.items(): #items 메소드로 dit 안의 키와 값을 k ,v 로 넣어준다.
#     print(k,v,sep = " ")