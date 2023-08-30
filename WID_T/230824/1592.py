N,M,L = map(int,input().split())


member = [0 for __ in range(N)]

count = 0 # 볼이 튕긴 횟수
ball= 0 # 볼의 위치


while member[ball]<M-1:
    count+=1
    member[ball]+=1
    ball= (ball+L)%N if member[ball]%2 ==1 else (ball-L)%N
    

    if member[ball] == M-1:
        break

print(count)

