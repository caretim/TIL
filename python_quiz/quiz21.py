# # 문제21

# > 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
# > 

# ### Input
# 1234


# ### Output
# 4321 

# 10으로 나눈 후에 나머지를 리스트에 저장 마지막에 숫자의 길이만큼 
# 리스트의 인덱스를 호출
# or  10을 곱한 후 인풋값을 뺀 후에 뺀 값을 숫자 자리를 바꿔 다시 더해준후 
#인풋 자리수만큼 곱하기 10을 해준 후 숫자 값을 앞에서부터 다시 빼준다.

n = int(input())
a= []
count= 0
while n :
    a.append(n%10) #n을 10으로 나눈 나머지를 a리스트에 넣는다
    n= n//10       #n은 10으로 나눠준 몫을 순환시킨다.
    count +=1      #n 카운팅을 통해 숫자의 자리수를 계산해준다
    # if n <1:
    #     break

for i in range(count): # 카운팅에 저장된 번호로 리스트 인덱스를 불러온다. 
    print(a[i],end='')


