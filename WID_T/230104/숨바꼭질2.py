from collections import deque

n, m = map(int,input().split())

r = n+m*4+1

check =[[-1,0]for __ in range(r)]




#점화식 = x-1, x+1 x*2
# 도착지점에 도달 한 순간부터 들어오는 m값을 체크 m값과 동일한 것만 넣어주고 그 이상의 시행은 멈춘다.
result = []

def find(n):
    q= deque()
    q.append((n,0))
    check[n][0]=1
    check[n][1]=0
    while q:
        v,j = q.popleft()
        for k in (v-1,v+1,v*2): 
            if 0<=k <r:
                if check[k][0] == -1:
                    check[k][0]=j+1
                    check[k][1]=1
                    q.append((k,j+1))
                elif check[k][0]==j+1:
                    check[k][1]+=1
                    q.append((k,j+1))

                # else: # 동생을 찾고나서의 로직 
                #     if  j+1 <= meet :
                #         if (k,j+1) == (m,meet):
                #             result.append(k)
                #         elif check[k]==0:
                #             q.append((k,j+1))

# collect = find(n,m)

# print()
find(n)
print(*check[m])
# print(find(n,m),len(result))




