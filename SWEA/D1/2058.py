
# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.


# [제약 사항]

# 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)


# [입력]

# 입력으로 자연수 N이 주어진다.


# [출력]

# 각 자릿수의 합을 출력한다.

n= int(input())

nsum= 0

while n != 0: # n이 != 0 이라면 참이 될떄까지 진행  n이 ==0이라면  무슨차이일까/
    nsum += n%10 
    n = n//10

print(nsum)

    