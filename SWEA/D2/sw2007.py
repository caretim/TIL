#패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

n= input()

dic= {}

for i in n:
    if dic not in i :
        dic[i]= 1
    else:
        dic[i]+=1 