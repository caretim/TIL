#N줄덧셈
# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.



# 주어진 숫자가 10 일 경우 출력해야 할 정답은,

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55



n= int(input())

nsum= 0
for i in range(n+1):
    nsum+=i
    

print(nsum)
