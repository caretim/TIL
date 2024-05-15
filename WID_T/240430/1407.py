

a,b =map(int,input().split())



# 간단하게 생각하면 각 값의 기본값 계산 , 현재 값에서 나눠지는 몫 + 홀수 일떄 더해지는 값 +1 , 

def calculate(x):
    two_times = 1 # 숫자 0+ 1  =  1 디폴트 1 값 설정
    res = x  
    while 2 ** two_times <= x:
        res += (x // (2 ** two_times)) * (2 ** (two_times - 1))
        two_times += 1
    return res

# f(A) + f(A+1) ... + f(B-1) + f(B)
print(calculate(b) - calculate(a - 1))



# def cal(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     elif x%2 == 0 :
#         return (x//2 +2) * cal (x//2)
#     elif x%2 == 1:
#         return (x//2+2)*cal(x//2)+1
