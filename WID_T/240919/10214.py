import sys

input =sys.stdin.readline




t = int(input())


for __ in range(t):
    point = [0,0]
    for i in range(9):
        s1,s2 =map(int,input().split())
        point[0]+=s1
        point[1]+=s2

    if point[0] == point[1]:
        print('Draw')
    elif point[0] > point[1]:
        print('Yonsei')
    else:
        print('Korea')