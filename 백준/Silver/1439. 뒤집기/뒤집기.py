lst = list(input())

one = 0
zero =0
change = ''
for i in range(len(lst)):
    if lst[i] == '0':
        if change != '0':
            change = '0'
            zero += 1
    else:
        if change != '1':
            change = '1'
            one += 1

print(min(one, zero))
