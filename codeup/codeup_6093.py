
# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

# 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부르는데,
# 영일이는 선생님이 부른 번호들을 기억하고 있다가 거꾸로 불러보는 것을 해보고 싶어졌다.

# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

# 예시
# ...
# for i in range(n-1, -1, -1) :
#   print(a[i], end=' ')
# ...

# 참고
# 번호를 부른 순서를 리스트에 순서대로 기록해 두었다가, 기록한 값들을 거꾸로 출력하면 된다.
# range(시작, 끝, 증감) #시작 수는 포함, 끝 수는 포함하지 않음. [시작, 끝)
# range(n-1, -1, -1) #n-1, n-2, ..., 3, 2, 1, 0


a = int(input())
b = map(int,input().split())

n= []
cnt= 0
for i in b:
  n.append(i) 
  cnt+= 1


for j in range(cnt-1,-1,-1):
  print(n[j],end=' ')
# for k in n:
#    k.append(str(n[i]))

# for j in range(n-1,-1,-1):
#   print (j)

# print (n)