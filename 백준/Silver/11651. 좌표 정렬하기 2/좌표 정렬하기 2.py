import sys
input = sys.stdin.readline

n= int(input())

xy_list =[]
for __ in range(n):
    x,y = map(int,input().split())
    xy_list.append((y,x))

xy_list.sort()
for y,x in xy_list:
    print(x,y)
