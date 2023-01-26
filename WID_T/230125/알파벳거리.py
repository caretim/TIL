
for tc in range(int(input())):


    a= list((input().split()))



    a1=[]
    a2=[]
    for k in a[0]:
        a1.append(ord(k)-64)
    for k in a[1]:
        a2.append(ord(k)-64)

    result = []

    for i in range(len(a1)):
        r = a2[i]-a1[i]
        if r >26:
            r= r-26
        elif r <0:
            r =26 + r
        result.append(r)
    result = ' '.join(map(str,result))
    distance = 'Distances: '

    print(distance+result)


