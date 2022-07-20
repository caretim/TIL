# 파벳으로 이루어진 문자열을 입력 받아 
# 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

#알파벳에 번호를 지정해서 IF문 돌리기  보다 딕셔너리로 돌리는게 편하겠다.


alpha= input()

abc = {}

n= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 딕셔너리로 알파벳과 숫자 묶어주기
cnt = 1
for char in n:

    abc[char]=cnt
    cnt +=1

for i in alpha:    
    print(abc[i],end=' ')  # 코드 작성시 값의 변수를 잘 확인하자 


# for abckey in abc.values(): # 굳이 포문돌려서 뽑을필요없이 print로 바로 출력하자
#     print(abc.values(r),end=' ')