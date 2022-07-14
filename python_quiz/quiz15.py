# 자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
# ### Input
# banana

# ### Output
# 1

# 아래의 테스트 케이스로도 확인 해보세요.
# apple # 0
# kiwi # -1
#  추가문제  - 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지




# word = input()

# a = 'a'

# s = 0
# c = len(int(input))
# for i in word : 
#     # for를 통해 i변수로 word 순환을 한다
#     s += 1
#     # 한번 순환 될때마다 s변수에 +1씩 추가된다 
#     if a in i :
#         #순환 되던중 a와 i 값이 같을 경우 s의 값을 출력시키고 if문 멈춤
#         print(s-1)
#         break

#     else :
    



word = input()

a = 'a'

s = 0
c = (len(list(word)))
for i in word : 
    # for를 통해 i변수로 word 순환을 한다
    s += 1
    # 한번 시행 될 때마다 s변수에 +1씩 추가된다 
    if a in i :
        #시행중 a와 i 값이 같을 경우  측정된 s값을 출력시킴 (이때 브레이크를 통해 측정을 멈춘다)
        print(s-1)
        break
    elif s == c :
        print(-1)
        

# # print(s)
#     if s == c :
#         # 그리고 입력된 글자수의 수와 반복문이 시행된 수 s 가 같아다면 -1 (a가 발견되어서 멈추면 s가 더 적을테니.)
#         print (-1)
#     else :
#         # a가 발견되었다면 반복된 수를 출력
#         print (s)
  


        
# len으로 길이를 확인하고  길이가 맞지 않으면 -1를 출력  
# if를 통해 a가 확인되면 a를 지워 길이를 하나 지운다. 
# 다시 길이를 측정해서 최초의 값과 같으면 -1를 출력한다. 맞지 않는다면 a의 위치를 출력
#