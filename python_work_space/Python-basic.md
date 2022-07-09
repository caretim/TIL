# Python -기초 

---



### 문자형 자료

 ' '는 그대로 출력하라 ex) 'pig' -> pig는 문자열이다.

" "문자형 자료 출력





## 타입

 숫자 관련 타입인 int와 float, 텍스트 타입인 str, 리스트 타입인 list



숫자라는 것은 4나 4.0이나 같은 것입니다. 하지만 파이썬에서는 다릅니다. 이 둘은 동시에 연산을 할 수 있기는 하겠으나, 값이 같을지는 몰라도 같은 타입은 아닙니다. **4는 정수**고, **4.0은 소수점**이 있는 수이기 때문이죠. 저흰 전자를 **int**라고 부르고 후자를 **float**이라고 부릅니다.





## 연산기호





---

**print(abs(-5)) # 5 abs 절대값**

**print(pow(4,2)) # 4^2 =4*4 =16 pow 제곱**

**print(max(5,12)) # 12 max 최대값**

**print(min(5,12)) # 5 min 최소값**

**print(round(3.14)) #3 round 반올림**

**print(round(4.8)) #5** 



from math import *(무슨뜻인지 확인하기)

**print(floor(4.99)) #내림 .4**

**print(ceil(3.14)) #올림. 4**

**print(sqrt(16)) #제곱근 4**



**print(2 +3 *4) #14**

**print((2+3)*4) #20**



### 변수 지정



변수

### 문제

파일을 다운로드할 때의 평균 속도(average rate)를 r이라 하고, 다운로드하는 데 걸린 시간(time)을 t라고 할 때, 다운로드한 파일의 용량은 r×t로 계산할 수 있습니다.

다운로드 속도가 초당 800kB이고 다운로드하는 데 걸린 시간이 110초라고 할 때, 다운로드한 파일의 크기는 몇 MB일까요? 단, 1MB=1000kB로 계산합니다.



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



### 인터프리터와 컴파일러

---

한마디 할 때마다 동시통역해주는 방식을 **인터프리트**(interpret) 방식이라고 하고, 말하는 것을 처음부터 끝까지 듣고 나서 한꺼번에 바꿔주는 것을 **컴파일**(compile) 방식이라고 합니다.





## while문 



```pyton 
num =1



while num <= 100:

  print(num)

  num = num +1
```



\#   #while은 어떤 조건이 만족되는 동안 그 아래에 쓴 문장들을 반복하는 기능을 갖고 있습니다. 여기서는 num이 100 이 될 때까지 print(num)과 num = num + 1을 반복하는 것이지요. 제가 반복을 해보겠습니다.



\# 처음엔 num 값이 1 이니까 100보다 작습니다. 그렇다면 그 다음 문장을 수행해야겠지요?



\# print(num) 이니까 화면에 1을 찍고 num = num + 1해서 num은 2가 됩니다.



\# 그리고는 다시 위의 while로 돌아가지요.



\# 그러면 num 값이 2 이므로 print(num)이 2를 찍고 num = num + 1해서 num은 3이 됩니다.



\# 그 다음엔 num 값이 3 이므로 print(num) 이 3을 찍고 num = num + 1해서 num은 4가 됩니다.



\# 그 다음엔 num 값이 4 이므로 print(num) 이 4를 찍고 num = num + 1해서 num은 5가 됩니다.그렇습니다.

\#  num이 100보다 작거나 같을 때 조건을 만족하는 겁니다.

\#  그러면 하던 일을 계속해야겠죠? print(num)하면 화면에 100을 찍고

\#  num = num + 1해서 num에는 101 이 들어갑니다. 그 다음에 while을 만나면



\#  이번엔 num이 100보다 크니까 그 다음의 문장을 수행하지 않고 끝이 나고야 맙니다.
