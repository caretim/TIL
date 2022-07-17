num = int(input())

count = 0
inum= 0

for i in range(num+1):
    count += 1
    inum = inum + i
    if inum >= num:
        print(count-1)
        break