import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x):
    global ans
    if (x not in arr and x != del_node):
        ans+=1
        return
    else:
        for i in range(n):
            if(arr[i]==x and i!=del_node):
                dfs(i)
    return ans

n = int(input())
arr = list(map(int, input().split()))
del_node = int(input())
start = arr.index(-1)
ans = 0
if(start == del_node):
    print(ans)

else:
    dfs(start)
    if (arr.count(arr[del_node])==1):
        ans+=1
    print(ans)