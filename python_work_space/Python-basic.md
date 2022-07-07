# Python -기초 

---



### 문자형 자료

 ' '는 그대로 출력하라

" "문자형 자료 출력



### 변수 지정

\#애완동물을 소개해주세요!

```python


age = 12

hobby = "산책"

animal = "강아지"

name = "꼬마"

is_adult = age >= 10


print("우리집에 " + animal + "가 있습니다 이름은 " + name + "에요")

print(name+ "는 나이가 " + str(age) +  "살이며, " + hobby +"을 좋아하고 간식을 좋아해요")

print(name+ "는 어른일까요? " + str(is_adult))

우리집에 강아지가 있습니다 이름은 꼬마에요
꼬마는 나이가 12살이며, 산책을 좋아하고 간식을 좋아해요    
꼬마는 어른일까요? True
우리집에  고양이 가 있습니다 이름은  버터 에요
버터 는 나이가  7 살이며,  간식 을 좋아하고 간식을 좋아해요
버터 는 어른일까요?  False
```





### 주석 

프로그램 코드안에 포함되어 있지만 실행은 되지 않는문장



#[코드]

 ''' 작은따옴표 3개 로 열고 ''' 3개로 닫으면 주석으로 나옴

``ctrl + /`` 를 통해 범위 주석처리 가능

ex )

#우리집에 강아지가 있습니다 이름은 꼬마에요

\# 꼬마는 나이가 12살이며, 산책을 좋아하고 간식을 좋아해요   

\# 꼬마는 어른일까요? True

\# 우리집에  고양이 가 있습니다 이름은  버터 에요

\# 버터 는 나이가  7 살이며,  간식 을 좋아하고 간식을 좋아해요

\# 버터 는 어른일까요?  False



## 문자열 

```pysentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"

print(sentence2)



sentence3 = """

 나는 소년이고,

 파이썬은 쉬워요

"""



print(sentence3)
```





### 슬라이싱 

---



jumin = "920627-1234567"



print("성별 : "+ jumin[7]) # 컴퓨터언어는 기본적으로 0부터 시작



print("연 : " +jumin[0:2]) # 0 부터 2 직전까지 



print("월 : " +jumin[2:4]) 



print("생년월일 : "+ jumin[:6]) # 처음부터 6직전까지 :(콜론으로시작하면)



print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지



print("뒤 7자리 (뒤에부터) : " +jumin[-7:] ) #맨 뒤에서 7번쨰부터 끝까지



### 문자열 처리 함수

---



python ="Python is Amazing"



print(python.lower()) #lower 함수는 문자를 소문자로 만듬



print(python.upper()) # upper 함수는 대문자로 만들어줌



print(python[0].isupper()) # isupper 파이썬의 0번째 문자가 대문자가 맞는지 알려주는 함수



print(len(python)) #파이썬의 글자 수 확인



print(python.replace("Python", "Java")) #replace 함수를 통해 바꾸고 싶은 글자를 바꿀 수있음



index = python.index("n") #N이 몇개가 있는지 인덱스 조회

print(index)



index = python.index("n", index + 1 )  # 앞의 인덱스에서 첫번째에서 다음 번째 n를 찾는 함수

print(index)



print(python.find("n")) # 원하는 변수가 없으면 -1로 표시됨

print(python.index("Python")) #원하는 변수가 없으면 에러가 뜸