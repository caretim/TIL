import sys
input = sys.stdin.readline

n, m = map(int,input().split())
n_cops,*cops = list(map(int,input().split()))

print(n_cops,cops)

cops = set(cops)
parties = []
available = [True] * m
for _ in range(m):
    _, *attendies = map(int,input().split())
    parties.append(set(attendies))

flag = True
while flag:
    flag = False
    for i in range(m):
        # party가 거짓말 가능성 있는데 cops과 member가 겹치면 not available
        # 그리고 그 파티의 member들은 cops에 합류
        # 이 변화로 다른 파티에도 영향 있을 수 있으니 flag = True로 다시 loop 돌기
        if available[i] and cops & parties[i]:
            available[i] = False
            flag = True
            cops = cops | parties[i]
            print(cops)
print(sum(available))