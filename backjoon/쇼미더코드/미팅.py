n,m,c = map(int,input().split()) # A대학총원 B대학총원  C사람들의 성격 수


matrix = [list(map(int,input().split())) for __ in range(c) ]


A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 학생의 수만큼 돌아야함, 인덱스는 추가되야하는점 이 어떻게 ?? i인덱스일때와 i인덱스 +1 일떄 
# 학교
result = []

h = A
l = B

if len(A)<len(B):
    h = B
    l = A
#i는 인덱스에 값이 추가되어야함
for i in range(len(h)-len(l)+1):
    count=0
    for j in range(len(l)):
        y=l[j]
        x=h[j+i]
        count+=matrix[y-1][x-1]
    result.append(count)


print(result)
print(max(result))


    
    



# 탐색은 값의 차에서 +! 
# a와 b의 차이값 +1 만큼 for문 돌리면서 각 인덱스노드를 순환하며 계산해주기,
# 숫자가 적은 학교은 정지  많은 학교는 순환 

# 인덱스 노드