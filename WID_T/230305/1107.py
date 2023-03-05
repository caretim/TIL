# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 


num = [0,1,2,3,4,5,6,7,8,9]
# 망가진 리모컨 버튼 숫자 빼기

# 1.남은 리모컨 숫자들로 채널에 가까운 숫자 만들기 ( 절대값으로 최소 값 구하기 )
# 1-1.리스트에서  |절대값|으로 가야할 채널에 가까운 숫자 만들기 -채널번호 for문 돌면서 가까운수, 
# 100에서 +1,-1로 움직여서 만들 수 있는 횟수 계산하기 -> 두개 넣어서 횟수 최소값 출력
# except = 채널번호가 100일경우 0 

n= int(input())

m= int(input())

k= list(map(int,input().split()))

result = []

for i in k:
    num.remove(i)

char=''

str_n=str(n)

for s in str_n:
    i = int(s)
    add_num =-1
    check_add = 10
    for j in num: # 흠 0이면 ? 상관없구나, 
        if abs(i-j)<check_add:
            check_add =abs(i-j)
            add_num =j
    char+=str(add_num)

result.append(abs(int(char)-n))

result.append(abs(n-100))

r = min(result)

if n == 100:
    r=0

print(r)


    


