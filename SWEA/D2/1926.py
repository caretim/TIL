# 3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.

 

# 1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.

#   1 2 3 4 5 6 7 8 9…

# 2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.  
# 예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
 

# 입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를

# 게임 규칙에 맞게 출력하는 프로그램을 작성하라.

# 박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.

# 여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 
n = int(input())
#  any(keyword in str for keyword in keywords)
re= []
inchar=[]
tsn= ['3','6','9']
for numbers in range(n):
    numbers_str=str(numbers+1)
    if any(tsns in numbers_str for tsns in tsn):# if tsn in numbers_str
        for num in range(len(numbers_str)):
            char= numbers_str[num:num+1] # 369가 들어간 숫자 자리별로 검사
            # char_int= int(char)
            if any(tsns in char for tsns in tsn):
                char= '-'
                inchar.append(char)
            else:
                pass
        b= ''.join(inchar) #두자리수가 들어가면 두번 반복함... 횟수여러번 시행했음..
        re.append(b)
        inchar.clear()
    else:
        re.append(numbers_str)
for jungdap in re:
    print(jungdap,end=' ') 

# def tsn():
#         if '3' or '6' or '9' in numbers_str:
#         for num in range(len(numbers_str)):
#             char= numbers_str[num:num+1]
#             char_int= int(char)
#         if char == 3 or char == 6 or char == 9:
#             char= '-'
#             inchar.append(char)
#         b= ','.join(inchar)
#         re.append(b)
#         inchar.clear()
#     else:
#         re.append(numbers_str)


