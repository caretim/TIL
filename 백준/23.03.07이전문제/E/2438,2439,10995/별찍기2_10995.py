

n= int(input())

star=' *'
for i in range(n):
    if i%2==0:
        print((star*n).lstrip())
    else:
        print((star*n))







# 짝수에는 앞에 공백이 하나가 들어감.
# 홀수일땐 첫공백이 없이 숫자만큼 별을 입력 