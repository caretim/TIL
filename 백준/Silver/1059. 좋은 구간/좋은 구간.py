L = int(input())
S = list(map(int,input().split()))
n = int(input())
answer = []

if n in S:
    print(0)
else:
    S.append(n)
    S.sort()
    index = S.index(n)
    if (index):
        prev = S[index-1]
    else:
        prev = 0
        
    N = S[index]
    next = S[index+1]
    
    for i in range(prev+1, N+1):
        for j in range(N, next):
            answer.append(((i,j)))

    print(len(set(answer))-1)