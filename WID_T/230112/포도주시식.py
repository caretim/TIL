n =int(input())


 # 인덱스 위치별로 점프 또는 더블 

wine = [0] 

# 최대 2까지 마시기 가능 

#점프는 2번쨰 인덱스 앞의 값 + 본인 점수
# 더블은 3전 최고값 + -1인덱스 점수 + 본인 인덱스 점수 
#i-1, i-2번째 포도주를 둘 다 왜 안먹어?? 먹어야지? 
for __ in range(n):
    wine.append(int(input()))


if n <3:
    print(sum(wine))
else:
    dp =[0,wine[1],wine[1]+wine[2]]
    for i in range(3,len(wine)):
        dp.append(max(dp[-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i]))

    print(max(dp))