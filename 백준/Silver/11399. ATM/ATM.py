


n = int(input())  

arr = list(map(int, input().split()))


result  = 0
arr.sort()  

for x in range(1, n+1):
    result += sum(arr[0:x])  
print(result)  