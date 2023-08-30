word = list(input())
result = []
for i in range(0,1):
    for j in range(1, len(word) - 1):
        for k in range(j+1, len(word)):
            char1 = list(reversed(word[i:j]))
            char2 = list(reversed(word[j:k]))
            char3 = list(reversed(word[k:]))
            sum_char = char1+char2+char3
            result.append(sum_char)

result.sort()
print("".join(result[0]))