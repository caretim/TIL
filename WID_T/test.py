import sys

input = sys.stdin.readline
t= int(input())



#같을 경우, 무조건 1부터 시작 
# 같을 경우 패스 ,
# 다를 경우 추가 , 
for tc in range(t):
    n = int(input())
    cnt= 0 
    nums=  list(map(int,input().split()))
    for i in range(1,201):
        if nums[cnt]!=i:
            cnt+=1
        if cnt == n:
            print(i)
            break

