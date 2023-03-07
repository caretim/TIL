#도비의 난독증 테스트 

while True:
    n= int(input())
    c1=[]
    c2=[]
    if n == 0:
        break
    else:
        for __ in range(n):
            ch= input()
            c1.append(ch)
            c2.append(ch.upper())
        c2.sort()
        for word in c1:
            a= str(word).upper()
            if a == c2[0]:
                print(word)

