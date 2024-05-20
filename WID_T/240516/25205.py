n= int(input())

s = input()

mo= 'yuiophjklnm'
result = 1
for m in mo:
    if m==s[n-1]:
        result =0
        break

print(result)