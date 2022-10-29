
def number_game(x,y):
    result = 0
    xresult = 0
    yresult = 0
    xlen= len(x)
    ylen= len(y)
    xsum = 0
    ysum = 0
    xmulti = 1
    ymulti = 1

    for i in range(xlen):
       xsum+=x[i] 
       xmulti*=x[i]

    for i in range(ylen):
        ysum+=y[i]
        ymulti*=y[i]

    if xsum >= xmulti:
        xresult = xsum
    else:
        xresult = xmulti


    if ysum >= ymulti:
        yresult = ysum
    else:
        yresult = ymulti

    if xresult < yresult:
        result= yresult
    else:
        result= xresult
    return (result)


pobi1, pobi2 =(input().split())

crong1, crong2 =(input().split())

pobi = number_game(pobi1, pobi2)

crong = number_game(crong1,crong2)

abscrong =  abs(crong1-crong2) 
abspobi = abs(pobi1-pobi2)

if abscrong > 1:
    print("-1")
elif abspobi >1:
    print("-1")
else:
    if pobi > crong:
        print("1")
    elif crong > pobi:
        print("2")
    elif crong == pobi:
        print("0")


