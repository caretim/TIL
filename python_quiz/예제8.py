# # 문제

# > 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.


# ### 오류 코드


# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# ### Output

#3

# 시행시 12개가 나옴 워드의 길이도 12 모든 문자가 다 카운트 되는것 같다.
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char =="e" or char =="i" or char =="o" or char =="u": 
#if char=='a'라는 참값 그리고 or "e", "i","o","u"는 
# 그 자체가 참값이 되기에 뒤까지 실행된다. or뒤에 조건을 걸어 참값을 변경시키자
        count += 1

print(count)
