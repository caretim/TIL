strs=[""]

sort_list = list(map(sorted,strs))


strs_set = set()
for i in sort_list:
    s = ''.join(i)
    strs_set.add(s)
 
result= [[] for __ in range(len(strs_set))]

strs_list = list(strs_set)

for i in range(len(sort_list)):
    result[strs_list.index(''.join(sort_list[i]))].append(strs[i])



