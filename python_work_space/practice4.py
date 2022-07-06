#애완동물을 소개해주세요!



age = 12
hobby = "산책"
animal = "강아지"
name = "꼬마"
is_adult = age >= 10



print("우리집에 " + animal + "가 있습니다 이름은 " + name + "에요")
print(name+ "는 나이가 " + str(age) +  "살이며, " + hobby +"을 좋아하고 간식을 좋아해요")
print(name+ "는 어른일까요? " + str(is_adult))



age = 7
hobby = "간식"
animal = "고양이"
name = "버터"
is_adult = age >= 10


'''이렇게 하면 
여러문장이 
주석처리
됩니다
'''

print("우리집에 "  ,animal,  "가 있습니다 이름은 " , name , "에요")
print(name, "는 나이가 " ,age,   "살이며, " , hobby ,"을 좋아하고 간식을 좋아해요")
#print(name, "는 어른일까요? " ,is_adult)
print(name, "는 어른일까요? " ,is_adult)


print(1 != 3) #True
print(not(1 != 3)) #False

print((3 >0)and (3<5)) #True
print((3>0)&(3<5)) # True

print((3>0)or(3>5)) # True
print((3>0)|(3>5)) #True

print(5>4>3) # True
print(5>4>7) #False



print(abs(-5)) # 5 abs 절대값
print(pow(4,2)) # 4^2 =4*4 =16 pow 제곱
print(max(5,12)) # 12 max 최대값
print(min(5,12)) # 5 min 최소값
print(round(3.14)) #3 round 반올림
print(round(4.8)) #5 

from math import *
print(floor(4.99)) #내림 .4
print(ceil(3.14)) #올림. 4
print(sqrt(16)) #제곱근 4

print(2 +3 *4) #14
print((2+3)*4) #20


number = 2 + 3 *4 #14
print(number) #14
number = number +2 #16
print(number)
number += 2 #18
print(number) #18
number *= 2 #36
print(number)
number /= 3 # 12
print(number)

number %= 7 # 5
print(number)