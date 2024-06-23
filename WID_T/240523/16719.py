# word= list(input())

# # 키밸류로 순서 정렬 후 각 글자 출력
# # 아스키 코드 기준 글자 정렬 후 각 글자에 매칭되는 글자의 밸류값 기준 정렬 
# #- > 단순하게 리스트와 순서의 값을 저장하고 각 순서를 람다함수로 순서 기준 정렬 후 출력

# start_word = ('z',80)
# o_word = []

# for i in range(len(word)):
#     if start_word[0]>word[i]:
#         start_word = (word[i],i)
#     o_word.append((word[i],i))


#  # 정렬된 단어
# visited= [0] *len(word)
# s = start_word[1] # 정렬된 워드중에 제일 앞쪽 

# prechar  = o_word[0:s]

# aftchar = o_word[s:]

# prechar.sort()
# aftchar.sort()

# print(prechar,'pre')
# print(aftchar,'aft')
# temp_word =   aftchar+prechar

# def char_sort(now):
#     global result



# tamp = []

# #놓친부분 단순하게 뒤에 슬라이싱 정렬 x 나오는 순서에서도 뒤쪽정렬먼저,
# for i in range(len(temp_word)):
#     tamp.append(temp_word[i])
#     tamp.sort(key =lambda x:x[1])
#     result = []
#     for i in tamp:
#         result.append(i[0])
#     print(*result,sep='')

s = input()

word = []
for i in range(len(s)):
    word.append((s[i], i))
word.sort()
result = []
result.append(word[0])
word.remove(word[0])
print(result[0][0])
while len(word) > 0:
    next_words = [result[:] for _ in range(len(word))]
    for i in range(len(word)):
        next_words[i].append(word[i])
        next_words[i].sort(key=lambda x: x[1])
    next_words.sort()
    showing = next_words[0]
    for i in word:
        if i in showing:
            word.remove(i)
            break
    for i in showing:
        print(i[0], end="")
    print()
    result = next_words[0]
