
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
    #cnt=0
    #recnt=0
    stack=[]
    visit[x]=True
    stack.append((x,1))
    cntls= []
    while stack:
        s =stack.pop()
        #cnt+=1
        #sq=0
        for j in node[s[0]]:
            if j==y :
                cntls.append(s[1])
            elif visit[j] == False:
                visit[j]= True
                stack.append((j,s[1]+1))
                #sq=1
        # if sq ==0:
        #     cnt-=recnt
        #     recnt=0
    #print(cntls)
    if len(cntls)>= 1:
        return min(cntls)
    elif len(cntls)==0:
        return '-1'
    

                

# print(node)
print(fam(ch1,ch2))