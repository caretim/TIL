n,k= map(int,input().split())


# 흠 이게 단순하게 큰수를 앞으로 되는 문제가 아니란걸 알겠는데 

#  제일 큰수만 바꿔서 넣으면 되는게 아닌가??? 흠 ..

# 선택정렬 가장 큰 수와 제일 작은수를 뒤로 움직이면 되는데

# 횟수만큼 수행 시행될떄마다 값은 자리가 무조건 바뀌어야한다.
#숫자가 0으로 시작 될 수 없음 

#1. 리스트 값 중 가장 큰 값과 작은 값을 자리 바꿈
#2. 리스트의 값중 2번째 큰 값을 맨 앞으로 가져옴 
#2-1 이미 완성된 숫자가 가장 큰 숫자 일 떄 마지막 2자리만 자리를 바꾸자

n_list= list(n)
mn = len(n)
r1=set()
r2=set()

for i in k:
    while 

