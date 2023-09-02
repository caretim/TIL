

n = 19
k = 0
num_set =set()
result = False
while k not in num_set:
    str_n = str(n)
    num_set.add(n)
    num = 0
    for i in range(len(str_n)):
        num += int(str_n[i])**2
    if num == 1:
        result = True
        break
    print(num)
    k = num
    n= num

print(result)
