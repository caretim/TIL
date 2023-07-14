count = [0] * 27

s = input()

for i in range(len(s)) :
  count[ord(s[i]) - 97] += 1

for i in range(26) :
  print(count[i], end=' ')