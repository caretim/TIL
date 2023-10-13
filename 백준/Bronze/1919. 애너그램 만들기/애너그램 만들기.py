
s1 = input()
s2 = input()

alphabet = [0]*26  # 알파벳저장 

for s in s1:
    alphabet[ord(s)-97] += 1

for s in s2:
    alphabet[ord(s)-97] -= 1

result = 0
for i in alphabet:
    result += abs(i)
print(result)