n = str(input())
s = int(input())


n_char = n[:-2]


for i in range(0, 100):
    i = str(i)
    if len(i) == 1:
        char = "0" + i
    else:
        char = i

    if int(n_char + char) % s == 0:
        # print(n_char, char)
        print(char)
        break
