import sys
input = sys.stdin.readline

N = int(input())
ants = [0] * 1_000_001
for _ in range(N):
    ant = int(input())
    if 0 <= ant <= 1000000: ants[ant] = 1

for i in range(1_000_001):
    if ants[i] == 0:
        print(i)
        break