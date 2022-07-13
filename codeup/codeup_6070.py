
# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

# 예시
# ...
# if n//3==1 :
#   print("spring")
# ...

# 참고
# 때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.
# winter = (12, 1 ,2)
# spring = (3,4,5)
# summer = (6,7,8)
# fall = (9,10,11)

# month = 3

# if month == winter :
#     print('winter')
# elif month == spring :
#     print('spring')
# elif month == summer :
#     print('summer')
# elif month == fall :
#     print('fall')


winter =  [12, 1,2] 
spring = [3, 5, 4]
summer = [6,7,8]
fall =  [9,10 ,11]
month = int(input())

if month in winter :
    print('winter')
elif month in spring :
        print('spring')
elif month in summer :
        print('summer')
elif month in fall  :
        print('fall')
