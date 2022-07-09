family = ['momther', 'father', 'ggoma', ' sister' ,'me'] 


print(len(family))

#len() 함수는 리스트에 원소(element)가 몇 개 들어 있는지 보여줍니다.
# 저희 가족을 family라는 리스트로 표현했으니까 5라고 대답을 하는 겁니다.

print(family[3])

#그럼 저희 가족 중에 넘버 쓰리가 누구인지 물어볼까요?

#아래와 같이 입력하고 Enter를 살짝 눌러주세요. print(family[3])

family.remove('me')
# remove는 뭔가를 제거한다는 뜻을 갖고 있죠. 위의 문장은 family에서 
# 'gentleman'이라는 놈을 없애라는 말입니다. 그럼 제가 확실히 없어졌는지 확인해보겠습니다.

print(family) 
#['momther', 'father', 'ggoma', ' sister']


