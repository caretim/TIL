

n = int(input())

treelist= list(map(int,input().split()))

d = int(input())

treeDict = dict()

for i in range(len(treelist)):
    if i not in treeDict:
        treeDict[i]= treelist[i]


def treeDelete(delete):
    for key,value in treeDict:
        if value == delete:
            
            treeDict[key]= -2



    