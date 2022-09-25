
n= int(input())



arr= []


for __ in range(n):
    x,y= input().split()

    arr.append((x,y))

arr.sort(key=lambda x:(x[1],x[0]))

for result in arr:
    if arr[0]==[1]:
        print(*result,sep=' ')