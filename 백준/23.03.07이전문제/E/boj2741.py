# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.


test_case= int(input())



for T in range(test_case):
    a,b= map(int,input().split())
    print(f'Case #{T+1}: {a+b}')