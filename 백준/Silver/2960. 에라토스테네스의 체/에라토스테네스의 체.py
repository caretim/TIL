n,k = map(int,input().split())

def solution(n,k):

    cnt = 0
    arr = [True] * (n+1)
    

    for i in range(2,n+1):
        if arr[i]:
            for j in range(i,n+1,i):
                if arr[j] == True:
                    arr[j] = False
                    cnt += 1
                    if cnt == k: return j
                    
print(solution(n,k))