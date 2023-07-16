string = str(input())
count = 0

for i in range(len(string)):
    if count == 9:
        print(string[i], end='')
        print("")
        count = 0
    else :
        print(string[i], end = '')
        count += 1