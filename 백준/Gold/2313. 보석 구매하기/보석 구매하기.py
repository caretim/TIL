

import sys
input =sys.stdin.readline

sum_score = 0
point =[]
for tc in range(int(input().rstrip())):
    n= int(input())
    jewel = list(map(int,input().split()))

    dp = [0]*n
    dp[0] = jewel[0]
    now =0
    for i in range(1,n):
        dp[i]=dp[i-1]+jewel[i]

    max_value= jewel[0]

    start,end= 0,0
    rs,re= 0,0


    for i in range(1,n):    
        if jewel[i]>= jewel[i-1]+jewel[i]:
            start,end= i,i
        else:
            jewel[i] = jewel[i-1] + jewel[i]
            end = i

        if jewel[i] > max_value:
            max_value=jewel[i]
            rs=start
            re=end
        elif jewel[i] == max_value and re - rs >end-start:
            mx =jewel[i]
            rs=start
            re=end
    sum_score+=max_value
    point.append((rs+1,re+1))


print(sum_score)

for p in point:
    print(*p)


        
    