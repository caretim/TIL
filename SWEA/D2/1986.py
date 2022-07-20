# 1부터 N까지 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값



# [제약사항]

# N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    nsum= 0
    for i in range(1,n+1):
        if i%2 ==0:
            nsum -= i
        elif i%2 !=0:
            nsum += i
    print (f'#{test_case} {nsum}') 
