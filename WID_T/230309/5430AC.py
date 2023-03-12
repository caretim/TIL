from collections import deque
import sys 

input = sys.stdin.readline

tc = int(input())

for __ in range(tc):
    fx = input() # 함수 
    n= int(input()) # 원소의 갯수 
    k = input()
    k= deque(map(int,eval(k)))
    count = 0 # 숫자 카운트 
    R= 1 #스택,큐 변환
    # if fx.count('D')>n: # 둘다 0 0 이라 흠,,빈칸처리될텐데, 
    #     print('error')
    #     continue
    count=0
    check =0
    for i in fx:
        if i=='D':
            if count+1>n:
                check =1
                break
            count+=1
            if R==1:
                k.popleft()
            elif R==-1:
                k.pop()
        elif i =='R':
            R=-R
    if check == 1:
        print('error')
        continue
    if R==-1:
        k.reverse()
    print('[', end='')
    print(*k, sep=',', end=']\n')

        # if len(result)>0:
        #     print('['+','.join(map(str,result))+']')
        # else:
        #     print('[]')
 
    

    