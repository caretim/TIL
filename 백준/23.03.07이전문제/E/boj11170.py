# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.

# 예를 들어, N, M이 각각 0, 10일 때 0을 세면 0에 하나, 10에 하나가 있으므로 답은 2이다.

for test in range(int(input())):
        
    x,y = map(int,input().split())

    cnt=0

    for i in range(x,y+1):
            cnt+=str(i).count('0') 

    print(cnt)