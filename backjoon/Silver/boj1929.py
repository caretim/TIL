#M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.


n,m  =map(int,input().split())

if n==1:
    n=2
    print(2)
elif n==2:
    print(2)
for num in range(n,m+1):
    cn=0
    if num%2 == 1:
        nsq= num**0.5
        for k in range(2,int(nsq)+1):
            if num%k==0:
                cn=1
                break
    if num%2 == 1 and cn==0:
        print(num)



