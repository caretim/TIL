import sys

input= sys.stdin.readline

n,m = map(int,input().split())

node =[[] for __ in range(m)]

for __ in range(m):
    i,j=map(int,input().split())
    node[i].append(j)



def dfs(t): #본인까지 돌아오는지 체크해야함, 
    can_list=[]
    check =[0]*n
    stack=[]
    stack.append(t)
    while stack:
        k= stack.pop()
        print(k[0])
        for i in node[k[0]]:
            if check[i]==0:
                stack.append(i)
                can_list.append(i)
                check[i]=1
    return(len(can_list))

result=0

dfs(node[0])