# 예제 2 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수
#  rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# * 사각형 넓이 : 가로 * 세로
# * 사각형 둘레 : (가로 + 세로) * 2

# a,b =map(int,input().split())

# def rectangle (a,b): 
#     return (a*b),((a+b)*2)

# c = rectangle(a,b)


# print(c)

#함수지정할 때 나중에 알아보기 쉽게 표기하기

a,b =map(int,input().split())

def rectangle (a, b): 
    area = a * b
    per = (a + b) * 2
    
    return area,per 

c = rectangle(a,b)


print(c)