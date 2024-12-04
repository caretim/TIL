import sys 

input= sys.stdin.readline

T = int(input())



for __ in range(T):
    cnt=0
    a = input()
    r,c = map(int,input().split())
    matrix = [list(input()) for __ in range(r)]
    for y in range(r-2):
        for x in range(c):
            if matrix[y][x] == 'v' and matrix[y+1][x] == 'o' and matrix[y+2][x] == '^':
                cnt += 1
    for y in range(r):
        for x in range(c-2):
            if matrix[y][x] == '>' and matrix[y][x+1] == 'o' and matrix[y][x+2] == '<':
                cnt += 1

    #             # if ord(matrix[y][x-1])+ord(matrix[y][x+1]) == 122:
    #             #     cnt+=1
    #             # if ord(matrix[y-1][x])+ord(matrix[y+1][x]) == 212:
    #             #     cnt+=1

print(cnt)