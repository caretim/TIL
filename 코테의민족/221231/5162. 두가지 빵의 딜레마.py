tc= int(input())

for test in range(1,tc+1):
    a,b,c= map(int,input().split())
    cheap = a
    if b<a: 
        cheap=b
    print(f'{test} {c//cheap}')


