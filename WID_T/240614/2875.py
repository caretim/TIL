n,m,k= map(int,input().split())


result = min(n//2,m)
mem = (n-result*2)+(m-result)
while k>mem or result>0:
    result-=1
    k-=3
    # if result ==0:
    #     break

print(result)