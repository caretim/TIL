s = "aabaab!bb"
# s ="pwwkew"
counter =0
result =""



for i in range(len(s)):
    if s[i] not in result:
        result+=result+s[i]
    else:
        for j in range(len(result)):
            if s[i] == result[j]:
                new_result =result[:j]
                result=new_result +s[i]
                break
    print(result)
    counter= max(counter,len(result))

print(counter)