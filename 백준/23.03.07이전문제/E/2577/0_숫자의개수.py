# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt")
# 곱한 값을 for문을 통해 숫자 문자열로 형변환하여 슬라이싱으로 각 숫자를 키값으로 분류
# 딕셔너리 1-9까지 키를 넣고 나온 숫자 만큼 밸류에 카운팅을 한 뒤
# 밸류값을 출력한다. 

#곱한 값을 10으로 나눠서 나머지 값만 인덱스 번호를 메겨서 추가해주는방법,

n1=int(input())
n2=int(input())
n3=int(input())
count_num=[0,0,0,0,0,0,0,0,0,0]

num = str(n1* n2* n3)  # 비교를 위해 문자열로 형변환


for i in range(len(num)):     # 형변환 한 문자열을 길이 측정 
    slicenum = num[i:i+1]     # 레인지를 통해 num의 문자열을 하나씩 가져옴
    intnum = int(slicenum)    # 인덱스에 넣어주기 위해 숫자로 변환시켜줌
    count_num[intnum]+= 1     # 변환된 숫자를 인덱스[숫자]로 매칭시켜 값을 하나씩 더해줌

for r in range(len(count_num)): #리스트의 값을 count_num의 갯수만큼 하나씩 방출
    print(count_num[r])


    # if i in conut_num:
    #     conut_num[i]=+ 1
    
    # else :
    #     count_num 

# print (conut_num)