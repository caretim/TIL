from itertools import permutations

n=int(input())

arr=list(map(int,input().split()))

u =list(map(int,input().split()))# 플러스 마이너스 곱하기 나누기

oper = []

fo =['+','-','*','/']
for i in range(4):
    for j in range(u[i]):
        oper.append(fo[i])

oper = list(set(permutations(oper,len(oper))))

result =[]

for o in oper:
    # print(o)
    r=arr[0]
    for k in range(len(arr)-1):
        if o[k] == '+':
            r+=arr[k+1]
        elif o[k] =='-':
            r-=arr[k+1]
        elif o[k] =='*':
            r*=arr[k+1]
        else: # '/' 나누기 일 때
            if r//arr[k+1]<0: # 음수일때 괄호계산을 안하기떄문에 먼저 연산 후 다시 마이너스 씌워주기 
                r=-(-r//arr[k+1])
            else: # 양수일떄는 그냥 나눠주기,
                r=r//arr[k+1]

    result.append(r)



print(max(result))
print(min(result))


