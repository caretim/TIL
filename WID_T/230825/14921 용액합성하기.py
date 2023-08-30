n= int(input())


arr = list(map(int,input().split()))


left = 0

right = len(arr)-1

min_value=1e9


while left <=right:
    if abs(arr[left]+arr[right])< abs(min_value):
        min_value= arr[left]+arr[right]
    if abs(arr[left])> abs(arr[left]):
        left+=1
    elif abs(arr[left])<abs(arr[right]):
        right-=1
    elif abs(arr[left])==abs(arr[right]):
        break

print(min_value) 