#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.


# for문으로 인풋 값을 리스트로 만들고 range로 배정해서 -1 넣어서 리스트순서를 
# 반전시켜 역순으로 출력되게 만들어보자 



# word = ['hello']
# # b= str(range[0:,-1])
# for i in word:
#     for rag in range(0,i):
#         print(rag)

        
# word = [1,2,3,4]
# l = len(word)

# # b= str(range[0:,-1])
# for i in word:
#     for rag in range(0):
#         print(rag)




# word1 = [1,2,3,4]
# # l = len(word)
# # ra = word(range(0,l+1,-1))
# for word in range(0,4,-1):


#  print(word)
word = ['hello']

#문자열을 앞에다가 더해주는 방법 
name = input()
n = '' # ''를 더해주는 이유가 뭘까

for c in name:
    n = c + n  # 순서대로 진행되는 걸 생각해서 c가 앞에 입력되도록하여 역순으로 만듬

print(n)