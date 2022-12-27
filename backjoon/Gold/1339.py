n = int(input())

word_list=[]

alpha_dic ={}

for __ in range(n):
    word_list.append(input())


for word in word_list:
    for i in range(len(word)):
        if word[i] not in alpha_dic:
            alpha_dic[word[i]] = 10**(len(word)-i-1) 
        else:
            alpha_dic[word[i]] += 10**(len(word)-i-1) 


alpha_value = sorted(alpha_dic.items(), key=lambda x: x[1], reverse=True)


