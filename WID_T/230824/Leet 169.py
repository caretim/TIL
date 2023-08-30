nums= [1,2,3,4,5,6,6,6]
dict={}
for n in nums:
    if n not in dict:
        dict[n] = 1
    else:
        dict[n]+=1

print(max(dict,key=dict.get))