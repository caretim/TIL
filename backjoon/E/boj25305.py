n,m= map(int,input().split())

sc = list(map(int,input().split()))


sc.sort(reverse=True)

print(sc.pop(m-1))