from math import factorial

#조합은  combination 사용도 가능
n= int(input())


for __ in range(n):
    n,m= map(int,input().split())
    bridge= factorial(m)//(factorial(n)*factorial(m-n)) # m!//(n!*(m-n)!)
    print(bridge)