

#가로로 리스트 확인하며 같은값 있는지 확인, x리스트 만들어서 길이값 넣기, 
# x고정값으로 y축을 확인, 만일 같은값이 존재한다면 길이 확인, 위의 값과 같다면 체크 같은길이로 각 좌표 체크 

n,m= map(int,input().split())


arr= [list(map(int,input())) for __ in range(n)]


def find(i,ii,rg,h,won):
    re = 0
    if h+rg< n and arr[h+rg][i] == won:
       if  h+rg< n and arr[h+rg][ii] == won:
           re= (rg+1)*(rg+1)
    return re        

   

result =[]

for h in range(n):
    dict ={}
    for i in range(m):
        if arr[h][i] not in dict:
            dict[(arr[h][i])]=i
        else:
            rg =i-dict[(arr[h][i])]
            k = find(i,dict[(arr[h][i])],rg,h,arr[h][i])
            if k >0:
                result.append(k)

if len(result)==0:
    print(1)
else:
    print(max(result))


