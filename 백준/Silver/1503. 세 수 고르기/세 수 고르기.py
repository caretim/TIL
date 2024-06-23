
import sys
input = sys.stdin.readline

INF = sys.maxsize
N, S = map(int,input().split())
num_list = set([i for i in range(1, 1002)]) -set(list(map(int,input().split())))
result = INF
for a in num_list:
    for b in num_list:
        for c in num_list:
            result = min(abs(N-a*b*c), result)
            if N+1 < a*b*c:
                break
print(result)