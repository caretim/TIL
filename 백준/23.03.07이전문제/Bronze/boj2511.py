a=[]
b=[]
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a_score=0
b_score=0
drawn = 0
drawAB= 0

for game in range(0,10):
    if a[game] > b[game] :
        a_score += 3
        drawAB= 'a'
    elif b[game] > a[game]:
        b_score += 3
        drawAB= 'b'
    elif a[game] == b[game] :
        a_score+=1
        b_score+=1
        drawn+=1
print(a_score,b_score,sep=' ')

if drawn == 10:
    print('D')
elif a_score > b_score:
    print('A')
elif b_score > a_score:
    print ('B')
elif a_score == b_score:
    print((drawAB))



