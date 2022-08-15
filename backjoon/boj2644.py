
n = int(input())

ch1,ch2= map(int,input().split())

m=int(input())

node= [[]for __ in range(n+1)]

visit= [False]*(n+1)

for __ in range(m):
    u,v= map(int,input().split())
    node[u].append(v)
    node[v].append(u)

def fam (x,y):
    cnt=0
    stack=[]
    visit[x]=True
    stack.append(x)
    while stack:
        s =stack.pop()
        cnt+=1
        sq=0
        for j in node[s]:
            if j==y :
                return cnt
            if visit[j] == False:
                visit[j]= True
                stack.append(j)
                sq=1
        if sq ==0:
            cnt-=1
    return -1
                


print(fam(ch1,ch2))