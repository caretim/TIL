# 입력
check_word = input()
n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input())
count = 0
for word in word_list:
    if (word * 2).find(check_word) != -1:
        count += 1
print(count)


# 입력
ring_str = input()
n = int(input())
rings = []
for _ in range(n):
    rings.append(input())
count = 0
# 똑같은 문자열 2개을 이어 붙이고 해당 문자열에 원하는 문자열이 있으면
# count+=1을 헤준다.
for ring in rings:
    if (ring * 2).find(ring_str) != -1:
        count += 1
print(count)
