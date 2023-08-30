# n,k= map(int,input().split())


# arr= list(map(int,input().split()))

# max_sum= 0


# for i in range(k-1,n):
#     temp = 0
#     for j in range(k):
#         arr[i-k]



N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = -100*K

total = 0
for j in range(K):
    total += arr[j]

if total > result:
    result = total


for i in range(0, N-K):
    total -= arr[i]
    total += arr[i+K]

    if total > result:
        result = total

print(result)