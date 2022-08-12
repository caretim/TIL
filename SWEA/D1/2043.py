
# 서랍의 비밀번호가 생각이 나지 않는다.

# 비밀번호 P는 000부터 999까지 번호 중의 하나이다.

# 주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.

# P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.




a, b = map(int, input().split())

sq= a-b

cnt= 0
for i in range(sq+1):
    cnt += 1
    
print(cnt)
