# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")


# 문자열로 for문 돌린 후 전의 문자열이 o라면 카운트 +1해서 하나씩 
# o라면 count + 1씩  x라면 값을 0으로 초기화 한후 더해줌
t = int(input())
for time_case in range(t):
    n= input()
    numlist= [] # 횟수가 반복 될때마다 점수가 리스트에 들어간다.
    count= 0    # 리스트에 들어갈 누적 카운트 값
    for i in range(len(n)): # OX의 길이를 측정
        for idx in n[i:i+1]: # 슬라이싱을 통해 각 자리수를 추출
            if idx == 'O':   # 각 자리수의 값이 O라면 +1 아니라면 카운트의 값을 0으로 되돌림
                count +=1    # O가 나오면다면 카운트에 +1을 누적함
                numlist.append(count) # 누적된 COUNT값을 NUMLIST에 추가해줌
            else:
                count=0     # O가 아닌 X나 다른값이 온다면 카운트는 0
    print(sum(numlist))     #리스트의 값을 모두 더한 후 출력 

            