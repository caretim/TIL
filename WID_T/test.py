def isPalindrome(s):
    word =[]
    for i in s:
        ii = ord(i)
        if 96<ii<123:
            word.append(i)
        elif 47<ii<58:
            word.append(i)
        elif 64<ii<91:
            word.append(i.lower())
    print(word)
    right=len(word)-1
    left = 0
    result= 'true'
    while left<right:
        if word[left] !=word[right]:
            result = 'false'
        right-=1
        left+=1
    return result

print(isPalindrome(s))
