from math import gcd

n = int(input())
rings = list(map(int, input().split()))

for i in range(1, n):
    x = gcd(rings[0], rings[i])
    print(f'{rings[0] // x}/{rings[i] // x}')