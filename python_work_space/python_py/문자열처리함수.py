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