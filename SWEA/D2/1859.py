#인덱스 값을 한번 진행할때마다 더해주는 값을 n*i (증가값 곱하기 더하기 횟수)

import sys


sys.stdin = open("input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n =int(input())

    price = list(map(int,input().split()))

    cnt=1 # 연달아 물건을 사야할때 카운트 다음 물건의 값이 크다면     
            #값을 cnt_price에 보내준뒤 0으로 초기화 # n

    sq= 0
    cnt_price= 0 # 
    low_price=[]

    for i in range(n):  #마지막 인덱스가 범위를 벗어나게됨.. 그럼 음수값으로 지정할까?
        if sq == n-1: # 작고 작을때 구매를 안하게됨 > > 
            break
        elif price[i] <= price[i+1] :
            p = price[i+1]-(price[i])
            cnt_price+= p*cnt
            cnt +=1 
            
        else :
            cnt =1
            
        sq +=1

    print(f'#{test_case} {cnt_price}')

    #처음부터 새로 짜야할듯. 리스트 최대값 최소값 만들어서 계산하는 코드짠거
#     len_num=int(input())
# n= list (map(int,input().split()))

# high=[]
# max_h=n[0]
# min_h=n[0]
# cnt= n[0]
# for nums in range(0,len_num) :
#     if n[nums] >= cnt:
#         cnt = n[nums]
#         max_h = n[nums]
        
#     elif n[nums]< cnt:
#         high.append(max_h-min_h)
#         cnt = n[nums]
#         min_h = n[nums]
#         max_h = n[nums]
# high.append(max_h-min_h)