n = int(input())

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

# S를 만들기 위한 최솟값, 각 숫자의 최소수,
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

A1 = sorted(A1, reverse=True)
A2.sort()


r = 0
for i in range(n):
    r += A1[i] * A2[i]
print(r)
