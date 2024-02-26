import sys

input =sys.stdin.readline



n= int(input())



arr = list(map(int,input().split()))

# 최초 시작에 각 배열에 1씩 증가시켜야함
#배열 최소값이 0이 될때까지 2로 나눈 상태에서 , 남은 횟수들을 더해주기,

# 1일경우 최대로 나눈 상태, check_Arr에서 거꾸로 연산하는게 빠름, 각 인덱스 요소를 반복문으로 2로 나누기



# min_arr = min(check_arr)

# while cnt_min%2:
#     cnt_min = min_arr//2

cnt = 0
while True:
    flag = True
    plus = False

    for i in range(n): #종료조건 체크
        if arr[i] !=0:
            flag =False
        if arr[i]%2 ==1: # 1 홀수 체크 
            plus =True
            cnt+=1
            arr[i]-=1
    if flag:
        break
    if not plus: # 홀수체크가 끝나고 나누기로 배열 값 0으로 만들기
        for i in range(n):
            arr[i]//=2
        cnt+=1

print(cnt)


    