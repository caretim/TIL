import sys

sys.stdin = open("input.txt", "r")
n_ori_len =int(input())

ori_num=[]
ori_num=list(map(int,input().split()))

n_oder =int(input())

oder_list=[]
oder_list=list(map(str,input().split()))

rnum = []

for i in range(len(oder_list)):
    if oder_list[i] == 'I':
        x= int(oder_list[i+1])
        y= int(oder_list[i+2])
        rnum.append(oder_list[i+3:i+3+y]) 
        for j in rnum[0]:
            ori_num.insert(x,j)
        rnum.clear()
print(ori_num)
        # ori_num.insert(oder_list[i+1],oder_list[i+3:i+3+[oder_list[i+2]]]) 
        # for r in (range(oder_list(int(i+3),int(i+3+y)))):

        # for r in oder_list:
        #     while True:

        #         n= oder_list[i+3] 
        #         ori_num.insert(x,n)
        # # for r in (range(oder_list(int(i+3),int(i+3+y)))):
        # # 인덱스는 숫자가 되어야한다.   
            
        # ori_num.insert(x,oder_list[i+3,i+3+y]) #틀리면 인덱스 확인
        # ori_num.insert(x,oder_list[i+3])
    # ori_num.insert(oder_list[i+1],oder_list[i+3:i+3+[oder_list[i+2]]]) 
# print(''.join(oder_list))
# print(ori_num[0:9])
 


# for oder in oder_num:
#     if oder == 'I':
#         oder_num[]
# I 0 4 600576 565945 486128 594841!  I 0 1 150706 ! I 8 8 556294 697547 932203 845517 116062 300371 621038 358830 
# ! I 10 8 747039 701738 805438 502654 476665 919177 367272 859931 !I 15 3 844423 973297 658751 



#1. I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에
#  y개의 숫자를 삽입한다.
#  s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]


