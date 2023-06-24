m, s = map(int, input().split(':'))




cnt = 1
cnt += (m//10 + m%10)
if s < 30:
    cnt += (s//10)
elif s >= 30:
    cnt += ((s-30)//10)

print(cnt)