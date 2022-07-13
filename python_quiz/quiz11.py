# #> 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.


# 1부터 9까지 리스트 만들고

#문제 11
# for문을 통해서 전체 순회

#f -string을 통해 'n단' 표시 -print (f'{a}단')
# for n in range를 통해서 숫자 나열할 값 만들기

# 한 숫자가 올때마다 
nine = (2,3,4,5,6,7,8,9)
# ran = range(1, 10)
# b= map(list(int,nine))

for i in nine :
    print (f'{i}단')
    for b in range(1,10):
         print(f'{i}x{b}=',(i*b))
    # print (b*ran)
   






