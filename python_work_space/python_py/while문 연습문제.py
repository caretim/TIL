
# i = 0         # 초기값 설정

# while i < 5:  # i가 5보다 작을때만 반복문 실행
#     print('* ' * 10)
#     i += 1




    
# num = 5

# i = 0
# while i < num:
#     print('', num)
#     i += 1


# 정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요.
#  단, while 문을 사용하세요. 
# 입력: 3
# 출력:
# 1 1
# 2 4
# 3 9



# 답안
# i = 0

# num= 4

# while i <= num:
#     print(i, i*i)
#     i += 1


# 고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다.
#  공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.

# 1 60.0
# 2 36.0
# 3 21.599999999999998
# 4 12.959999999999999
# 5 7.775999999999999
# 6 4.6655999999999995
# 7 2.7993599999999996
# 8 1.6796159999999998
# 9 1.0077695999999998
# 10 0.6046617599999998

# 내 답안
high = 100
bounce = 10
i = 1

while i<=bounce:
    print(round (high,4))
    high= high*0.6
    
    i += 1

#  모범답안
# height = 100
# bounce = 3 / 5

# i = 1

# while i <= 10:
#     height = height * bounce
#     print(i, round(height, 4))
#     i = i + 1
number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)