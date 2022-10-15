


from collections import deque




def dfs(y,x):
    q= deque()
    q.append((y,x))


    


shop = int(input())

start_y, start_x = map(int, input().split())


con = []

for __ in range(shop + 1):
    y, x = map(int, input().split())
    con.append((y, x))



# 간단하게 연산으로만 풀기,


n = int(input())

yard = []

bw = 1000
1
for __ in range(n + 2):
    y, x = map(int, input().split())
    yard.append(y + x)

now = yard[0]

0 - 1000

finish = yard[n + 1]  # 인덱스 시작 0
for i in range(1, n + 2):
    if now - yard[i] >= -1000:  # 400 1300
        print("sad")
    elif now - yard[i] <= -1000:
        now = yard[i]
        pass
print("happy")
