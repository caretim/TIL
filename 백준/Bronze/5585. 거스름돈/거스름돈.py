pay = 1000 - int(input()) # 1000 380 -> 620 , 4
cnt = 0
x = [500,100,50,10,5,1]
for i in x:
    cnt = cnt + pay // i
    pay = pay % i
print(cnt)