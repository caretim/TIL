from collections import deque
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 


num = [0,1,2,3,4,5,6,7,8,9]
# 망가진 리모컨 버튼 숫자 빼기

# 1.남은 리모컨 숫자들로 채널에 가까운 숫자 만들기 ( 절대값으로 최소 값 구하기 )
# 1-1.리스트에서  |절대값|으로 가야할 채널에 가까운 숫자 만들기 -채널번호 for문 돌면서 가까운수, 
# 100에서 +1,-1로 움직여서 만들 수 있는 횟수 계산하기 -> 두개 넣어서 횟수 최소값 출력
# except = 채널번호가 100일경우 0 
num = [0,1,2,3,4,5,6,7,8,9]
n= int(input())

m= int(input())
if m >0:
    k= list(map(int,input().split()))
else: 
    print(len(str(n)))
    exit(0)
result = []

for i in k:
    num.remove(i)

char=''

str_n=str(n)

for s in str_n:
    i = int(s)
    add_num =-1
    for j in num: 
        an =  abs(i-j)
        if an ==0 :
            add_num=j
            break
    if add_num == -1:
        break
    else :
        char+=str(add_num)


snc = int(str_n)
if snc ==0:
    snc = 0
sc = len(char)
if sc ==0:
    sc = 0

new_char =''
for __ in range((snc-sc)):
    new_char+='0'

inc = int(new_char)
if inc ==0:
    inc = 0

min_n = 500001
min_cn =0

for i in range(int(new_char),1000000):
    str_i = str(i)
    count=0
    for si in str_i:
        if int(si) in num:
            count+=1
    if count == len(str_n):
        if min_n>abs(n-i):
            min_n=abs(n-i)
            min_cn =i

    
    
            


    
# 놓친점, 절대값으로 구하는건 좋으나, 플러스 or 마이너스로 진행될지 모름, 
# 숫자 인덱스를 늘릴때마다 n과 추가된 숫자를 계산해주기, 흠 근데 절대값으로하면 똑같을텐데? 
# num리스트안의 숫자에 따라서 바뀔텐데, 그러면 흠,, -1 ,1 나눠서 이분탐색? 
# -1의 경우와 +1의 경우 -와 +가 결정되는 순간이 언제일까?
# 마이너스와 플러스 분기가 결정되는 순간 절대값으로 움직이는게아니라,

# 분기에 따라  인덱스보다 가까우며 보다 큰수 또는 보다 작은수 를 추가해야함
# 절대값으로 탐색하다가, 분기가 갈리는순간, 큰수로 구성 또는 작은수로 구성을해야한다. 
# 동일한 값 가지고 있다가 최소 절대값기준으로구성, 절대값이 동일 할떄 - + 처리,등장시, s로 삽입 후 백트레킹, 

result.append((min_n+len(str_n)))

result.append(abs(n-100))

r = min(result)

if n == 100:
    r=0

print(r)





# num = [0,1,2,3,4,5,6,7,8,9]
# n= int(input())

# m= int(input())

# k= list(map(int,input().split()))

# result = []

# for i in k:
#     num.remove(i)



# for i in range(0,500001):
#     str_i = str(i)
#     count=0
#     for si in str_i:
#         if int(si) in k:
#             break
#         else:
#             count+=1
#     if count == len(str_n):
#         if min_n>abs(n-i):
#             min_n=abs(n-i)
#             min_cn =i
#             print(i)