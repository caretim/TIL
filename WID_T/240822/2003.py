n, m = map(int, input().split())
s = list(map(int, input().split()))
ans = 0
l = 0
r = 0

while(r<n):
    k = sum(s[l:r+1])
    if k == m: 
        ans += 1
        r += 1
    elif k > m:
        l += 1
    else:
        r += 1
    
print(ans)