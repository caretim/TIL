import sys
def primeFactorization(n):
    for i in range(2, n+1):
        if n % i == 0:
            if i not in prime.keys():
                prime.setdefault(i, 1)
            else:
                prime[i] += 1
            primeFactorization(n//i)
            break
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    prime = dict()
    primeFactorization(n)
    for k, v in prime.items():
        print(k, v)