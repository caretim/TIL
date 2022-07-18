# > 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# > 

# ### 오류 코드


# numbers = input().split()
# print(sum(numbers))


# ### Input
# 10 20


# ### Output
# 30
 
numbers=map(int,input().split()) # sum은 int타입만 가능하다.  type에러발생
                                 # map을 사용해 int로 구성된 리스트로 만들자

print(sum(numbers))

 
