n = int(input())
num = list(input().split())


check = int(input())
check_num = list(input().split())

dict={}

for i in num:
    dict[i]= 1


for i in check_num:
    try:
        dict[i] == 1
        print(1)
    except:
        print(0)

