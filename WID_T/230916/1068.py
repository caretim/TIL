from collections import defaultdict
n = int(input())

nodeDict = defaultdict(list)


nodeList = list(map(int,input().split()))



for i,parents in enumerate(nodeList):
    if nodeList[i] ==-1:
        root = i 
    nodeDict[parents].append(i)

delete_node =int(input())

try:
    del nodeDict[delete_node]
except:
    pass


result=[]

def find(node):
    if node == delete_node:
        return
    if len(nodeDict[node])==0:
        result.append(node)
    for i in nodeDict[node]:
        find(i)

    
find(root)
print(result)
print(len(result))