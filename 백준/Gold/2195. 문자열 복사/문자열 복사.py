import sys
S = list(sys.stdin.readline().strip())
P = list(sys.stdin.readline().strip())
min_ = 2000
idx = 0
tot = 0
while True:
    if idx == len(P):
        break
    tmp = idx
    start = idx
    flag = 0
    for i in range(len(S)):
        if start == len(P):
            break
        if S[i] == P[start]:
            start+=1
            flag = 1
        elif flag == 1 and S[i] != P[start]:
            idx = max(idx,start)
            start = tmp
            flag = 0
    idx = max(idx,start)
    tot+=1
print(tot)