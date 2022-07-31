n = int(input())

word_ls =[]

word_dc = {}
for __ in range(n):
    n_= input()
    word_ls.append(n_)

for i in word_ls:
    if i not in word_dc:
        word_dc[i]= len(i)



char = max(word_dc.values())


for reselt in range(1,char+1):
    lenword=[]
    for idx in word_dc:
        if word_dc[idx] == reselt:
            lenword.append(idx)
    lenword.sort()
    for r in lenword:
        print(r)