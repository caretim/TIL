

n= int(input())


numCounter= [0]*(10)

#자리수   자리수의 값 + (len(n) - i +1) ^ 10 
#입력된 수가 3444일떄, 4끝자리 4 각 번호 1씩 더해주기, 10자리 일때 각 번호 + 10 더해주기,  
# 1000일경우
# 1의 자리수는 0-9의 모든수 +=1 -> 1의 자리수에서 이미 더해짐,
# 10의 자리수는 0-9의 모든수 += 10 -> 10번 
# 100의 자리수는 0-9의 모든수 += 100  


#91일 경우
# 1의 자리수 +1
# 10의자리수 9 이므로 모든자리수에 9번 더해주기, 
# 자리수를 하나씩 구분하기  힘드니 각 자리를 9로 맞춘후 각 자리의 차이 , 
# n의 1의 자리수와 9까지의 자리수에서 -1 해주기,
# 0의자리수 각자리수에 0뺴주기, 

#각자리에 더해줄 페이지 수 
# addCount = 1

# #전체의 값 
# for i in range(len(n)):
#     j = len(n)-i
#     for j in range(int(n[i])):
#         if i == 0:
#             numCounter[j]+= 1
#         else:
#             print('실행')
#             numCounter[j]+= addCount

#     #0자리수 빼주기
#     numCounter[0]-=addCount
#     #자리수 10 곱해주기,
#     addCount*=10




addPage = 1
for step in range(len(str(n))):
    # 끝자리수 9로 변경
    replaced = int(str(n // 10) + "9")
    R = replaced - n
    # 현재 값의 앞자리수만큼 페이지 갱신
    for i in range(len(numCounter)):
        numCounter[i] += (n // 10 + 1) * addPage
    # 현재 자리수의 뒤의값 페이지 값 갱신 
    for i in range(10-R, 10):
        numCounter[i] -= addPage
    # 현재 자리수의 앞자리 수 값 갱신 
    for number in list(str(n)[:-1]):
        number = int(number)
        numCounter[number] -= R * addPage
    #자리수 변경 루틴 
    numCounter[0] -= addPage
    n //= 10
    addPage *= 10

print(*numCounter,sep=" ")