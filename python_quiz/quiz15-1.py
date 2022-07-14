#추가문제

#  추가문제  - 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지


word = input()

a = 'a'
list = []
s = 0
# c = (len(list(word)))
for i in word : 
    # for를 통해 i변수로 word 순환을 한다
    s += 1
    # 한번 시행 될 때마다 s변수에 +1씩 추가된다 
    if a in i :
        #시행중 a와 i 값이 같을 경우 s값을 list에 추가해줌 **print를 통해서 바로바로 출력하는방법
        list.append(s-1)

# e = str(list)[1:-1] #! 삽질
# print(e,sep=" ",end=" ") #출력값이 한 값으로 묶여 있어서 공백으로 표기가 안된다. for문을 통해 list를 뽑자

for r in list:
    print(r,end=" ")

       

        