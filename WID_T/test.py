n = int(input())

min_cnt = 4

def dv(n, cnt):
    global min_cnt
    if n == 0:
        min_cnt = min(min_cnt, cnt)
        return
    if cnt > min_cnt:
        return
    for i in range(int(n ** 0.5),int((n//(4-cnt)) ** 0.5),-1):
        dv(n - i**2,cnt+1)
    
dv(n,0)
print(min_cnt)