
check_word = input()
n = int(input())
word_list =[]
for _ in range(n):
    word_list.append(input())
count = 0
for word in word_list:
    if (word*2).find(check_word) != -1:
        count+=1
print(count)
