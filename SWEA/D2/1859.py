#인덱스 값을 한번 진행할때마다 더해주는 값을 n*i (증가값 곱하기 더하기 횟수)


n =int(input())

price = list(map(int,input().split()))

cnt=1 # 연달아 물건을 사야할때 카운트 다음 물건의 값이 크다면     
        #값을 cnt_price에 보내준뒤 0으로 초기화 # n


cnt_price= 0 # 

for i in range(n):  #마지막 인덱스가 범위를 벗어나게됨.. 그럼 음수값으로 지정할까?
    if price[i] <= price[i+1] :
        p = price[i+1]-(price[i])
        cnt_price+= p*cnt
        cnt +=1 
    else :
        cnt =0

print(cnt_price)