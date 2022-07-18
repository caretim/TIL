# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count) # 출력했을시 55가 나옴 

# ### Output
# 5.5

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0 # 시행했을시 토탈은 55가 된다
count = 0

for number in number_list:
    total += number
    count += 1   #카운트가 for문 종속으로 되어있지 않아서 한번 시행됨

# //는 몫만 나온다 / 로 바꿔주고 float으로 실수로 형변환시켜줘야 소수점까지 나옴
print((float(total / count)))