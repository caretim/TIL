import sys

n= int(input())


matrix =[list(map(int,input().split())) for __ in range(n)]


#1- 비숍가능 0 - 비숍불가능  -체스판에 놓을 수 있는 최대 비숍의 개수 구하기
# 대각선 한방향으로 존재할 수 있는 비숍 2n-1
# 각 대각선의 꼭지점 위치 각 하나씩 가능  각 기울기를 visited로 놓기?

