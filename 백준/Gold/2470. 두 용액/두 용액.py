import sys
n= int(input())

arr =list(map(int,input().split()))

arr.sort()

def double_pointer(arr):
    l=0
    r=n-1
    result=[arr[l],arr[r]]
    while l<r: #교차점까지 진행,
        if abs(arr[l]+arr[r])<abs(sum(result)): # l은 음수, r은 양수시작,
            result =[arr[l],arr[r]]
        if abs(arr[l])>abs(arr[r]): # 오른쪽수가 크다면 왼쪽포인터 증가,
            l+=1
        else: # 왼쪽수가  크다면 오른쪽 포인터 감소 
            r-=1
    return result

print(*double_pointer(arr))