
n= int(input())



arr= []


for __ in range(n):
    age,name= input().split()

    arr.append((age,name))

arr.sort(key=lambda x:x[0])

for result in arr:
    print(*result,sep=' ')

    