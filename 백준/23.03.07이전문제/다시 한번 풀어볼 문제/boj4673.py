

# self_num =[]

# for number in range(1,100):
#     nl = len(str(number))
#     cr_num=[1]
#     if number >=19:
#         for num in range(number-(nl*9),number):
#             count=0
#             nums=num
#             while True:
#                 count += nums%10
#                 nums = nums//10
#                 if nums==0:
#                     break
#             if num+ count== number:
#                 cr_num.append(num)
#                 break
#             print(cr_num)
#     elif number <19:
#             pass     
#     if len(cr_num) == 1 :
#         self_num.append(number)

# # print(self_num)
              
self_num=[]

for number in range(1,10001):
    self_num.append(number)


for numbers in range(1,10001):
    count=0
    con= numbers
    while True:
        count += con%10
        con= con//10
        if con==0:
            break
    if count + numbers in self_num:
        self_num.remove(count + numbers)

for reselt in self_num:
    print(reselt)
## 변수값 numbers을 그대로 가져와서 while문을 돌렸더니 numbers이 계속변하여 제대로된 값을 지우지 못했다.
# 변수의 움직임을 잘 생각해보자 