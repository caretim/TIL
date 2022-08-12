

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
            

    date=input()
    y= int(date[0:4])

    m= int(date[4:6])
    d= int(date[6:])



    if m > 12 or m <= 0 :
        print('-1')
    elif m == 2 :
        if d < 1 or d > 28 : #elif 문 아래에 if문을 중첩하니 실행하다가 멈춤 이유가 뭐지?
            print('-1')    
        else:
            print(f'#{test_case} %04d'%y,'%02d'%m,'%02d'%d,sep=('/')) # False일때는 정상 출력됨 ,상위의 elif를 if로 바꿔도 정상실행됨
    elif d > 31 or d < 1 :
            print('-1')
    elif m in [4,6,9,11] :  # 그룹을 바꾸거나 or m==4 , m==6을해도 시행이 안됨 
        if d < 1 or d > 30 : # 이것도 마찬가지로  False일때는 정상출력 True일때는 출력 안됨
            print('-1')
        else:
            print(f'{test_case} %04d'%y,'%02d'%m,'%02d'%d,sep=('/'))
    else :
        print(f'#{test_case} %04d'%y,'%02d'%m,'%02d'%d,sep=('/'))
    






# elif d < 10 and m < 10:
#     print(f'#{test_case} {y}/0{m}/0{d}')
# elif d < 10:
#     print(f'#{test_case} {y}/0{m}/{d}')
# elif d < 10:
#     print(f'#{test_case} {y}/{m}/0{d}')
# elif y < 100:
#     print(f'#{test_case} 00{y}/{m}/0{d}')
# elif y < 1000:
#     print(f'#{test_case} 0{y}/{m}/{d}') # 삽질했음..
# else :
#     print(f'#{test_case} {y}/{m}/{d}')


# date=input()
# y= (date[0:4])
# m= (date[4:6])
# d= (date[6:8])

# gy= []
# gm= []
# gd =[]

# for years in range(0,10000):
#     gy.append[years]
# for mons in range (1,12):
#     gm.append[mons]
# for days in range (1,31):
#     gd.append[days]

# str_gy= list(map(str,gy))
# str_gm= list(map(str,gm))
# str_gd= list(map(str,gd))

# if 

# print(f'{y}/{m}/{d}')

