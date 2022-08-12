# 여덟 자리의 양의 정수가 주어질 때, 그 안에서 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하고, 있으면 같은 숫자가 연속해서 나오는 구간 중 가장 긴 것의 길이를 출력하는 프로그램을 작성하라. 

# 예를 들어 세 개의 숫자 12345123, 17772345, 22233331이 주어졌다고 하자. 12345123은 연속하여 같은 숫자가 나오는 것이 없으므로 1을 출력하고, 17772345는 7이 세 개 연속하여 나오므로 3을 출력하며, 22233331의 경우에는 2가 세 개, 3이 네 개 연속해서 나오므로 그 중 큰 값인 4를 출력하여야 한다.  




# for __ in range(3):
#     number =input()
#     cnt= [0]*10
#     for n in number:
#         cnt[int(n)]+=1




for __ in range(3):
    number =input()
    numlist=[0]
    cnt=0
    for n in range(0,len(number)-1):
        if number[n] == number[n+1]:
            cnt+=1
        elif number[n] != number[n+1]:
            numlist.append(cnt)
            cnt=0
    numlist.append(cnt)

    if max(numlist)== 0:
        print('1')
    else :
        print(max(numlist)+1)