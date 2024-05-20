import sys
import copy
input =sys.stdin.readline


n= int(input())





#각 트리 노드 탐색, 현재 스택에 들어있는 값 제외한 나머지 값으로 이뤄지는 수열


stack = []
def backtraking(m):
    if len(stack)==m:
        print(' '.join(map(str,stack))) # 현재 함수 종료조건 - 문제의 최대 길이 도달시 
        return
    for i in range(1,n+1):  
        if i not in stack:   #현재 값이 스택에 안들어가 있다면, 값 추가 후 재귀적으로 탐색시행
            stack.append(i)
            backtraking(m)   
            stack.pop()

n,m = map(int,input().split())
backtraking(m)
 
