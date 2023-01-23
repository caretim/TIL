

import sys 
input = sys.stdin.readline

for tc in range(int(input())):
    h,w,n= map(int,input().rstrip().split())


    count= n
    for x in range(1,w+1):
        for y in range(1,h+1):
            count-=1
            if count==0:
                if x <10:
                    x = str('0')+str(x)
                print(f'{y}{x}')  
                break

        


