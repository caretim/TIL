
num =1

while num <= 100:
    print(num)
    num = num +1

#     #while은 어떤 조건이 만족되는 동안 그 아래에 쓴 문장들을 반복하는 기능을 갖고 있습니다. 여기서는 num이 100 이 될 때까지 print(num)과 num = num + 1을 반복하는 것이지요. 제가 반복을 해보겠습니다.

# 처음엔 num 값이 1 이니까 100보다 작습니다. 그렇다면 그 다음 문장을 수행해야겠지요?

# print(num) 이니까 화면에 1을 찍고 num = num + 1해서 num은 2가 됩니다.

# 그리고는 다시 위의 while로 돌아가지요.

# 그러면 num 값이 2 이므로 print(num)이 2를 찍고 num = num + 1해서 num은 3이 됩니다.

# 그 다음엔 num 값이 3 이므로 print(num) 이 3을 찍고 num = num + 1해서 num은 4가 됩니다.

# 그 다음엔 num 값이 4 이므로 print(num) 이 4를 찍고 num = num + 1해서 num은 5가 됩니다.그렇습니다.
#  num이 100보다 작거나 같을 때 조건을 만족하는 겁니다.
#  그러면 하던 일을 계속해야겠죠? print(num)하면 화면에 100을 찍고
#  num = num + 1해서 num에는 101 이 들어갑니다. 그 다음에 while을 만나면

#  이번엔 num이 100보다 크니까 그 다음의 문장을 수행하지 않고 끝이 나고야 맙니다.

# input()으로 사용자로부터 정수를 한 개 입력받아, 그
#  숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 
# 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
# 단, while 문을 사용하세요.

# input= 3

# while input > input:
#     print(input)



num = int(input())

i = 0
while i < num:
    print('', num)
    i += 1