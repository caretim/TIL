from tkinter import Y


n= int(input())


matrix=[list(map(int,input().split())) for __ in range(n)]


for y in range(n):
    for x in range(n):
        if matrix[y][x]> n: