N = int(input())
# 위 삼각형
for i in range(1, N+1):
    print("*"*i)

# 아래 삼각형
for i in range(1, N):
    print("*"*(N-i))