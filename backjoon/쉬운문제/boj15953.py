# 카카오 코드 페스티벌에서 빠질 수 없는 것은 바로 상금이다. 2017년에 개최된 제1회 코드 페스티벌에서는, 본선 진출자 100명 중 21명에게 아래와 같은 기준으로 상금을 부여하였다.
# # 순위	상금	인원
# 1등	500만원	1명
# 2등	300만원	2명
# 3등	200만원	3명
# 4등	50만원	4명
# 5등	30만원	5명
# 6등	10만원	6명
# 2018년에 개최될 제2회 코드 페스티벌에서는 상금의 규모가 확대되어, 본선 진출자 64명 중 31명에게 아래와 같은 기준으로 상금을 부여할 예정이다.

# 순위	상금	인원
# 1등	512만원	1명
# 2등	256만원	2명
# 3등	128만원	4명
# 4등	64만원	8명
# 5등	32만원	16명

n= int(input())

for __ in range(n):
    count=0
    a,b = map(int,input().split())
    if a == 0:
        pass
    elif a ==1 :
        count+= 500
    elif a <= 3:
        count+= 300
    elif a <= 6:
        count+= 200
    elif a <= 10:
        count+= 50
    elif a <= 15:
        count+= 30
    elif a <= 21:
        count+= 10
    else:
        pass

    if b == 0:
        pass
    elif b ==1 :
        count+= 512
    elif b <= 3:
        count+= 256
    elif b <= 7:
        count+= 128
    elif b <= 15:
        count+= 64
    elif b <= 31:
        count+= 32
    else:
        b <= 0
        pass
     
    print(count*10000)
