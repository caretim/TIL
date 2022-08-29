n= int(input())


arr= []


nums =[]

result=[]


for ne in range(n):
    arr.append(ne)


for num in range(n):
    if num == arr[0]: # 숫자와 어레이의 첫숫자가 같다면 
        a=arr.pop(0)    # 어레이 에서 첫숫자를 팝 . #그리고 nums리스트에 추가를 안해준다.
        result.append('-') # result 리스트에 - 추가 
        if arr[0]< a:
            if arr[0]==nums.pop():
                
    else:
        nums.append(num) # 어레와 숫자가 같지 않다면 넘즈 +1 
