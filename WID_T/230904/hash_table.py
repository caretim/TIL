class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value


# ”Hash Table의 크기는 2의 멱수 (2^0, 2^1, 2^2...2^11에 가깝지 않은 소수(prime number)”를 선택하는 것이 좋습니다.
class Linear_Probing_Hash_table:
    def __init__(self,length= 97): # 97 테이블 크기만큼 나눈다
        self.max_len = length     #테이블 key를 97로 나누어 해싱
        self.table = [[0] for __ in range(length)]

    def hash(self,key): #해시테이블에 key와 value넣기.
        hash_key = sum([ord(i) for i in key])
        return hash_key % self.max_len # #ord함수로 문자열 변경후 나온 값  % max_len

    def add(self,key,value):
        index = self.hash(key)
        if self.table[index]!=0:
            for i in range(index,self.max_len):
                if self.table[i]==0:
                    self.table[i] = [key,value]
        else:
            self.table[index]=[key,value]

    def put(self,key,value):
        index = self.hash(key)
        if self.table[index]==0:
            return None # 데이터 존재하지 않음
        else:
            for i in range(index,self.max_len):
                if self.table[i][0]==index: #변환된 인덱스부터 밑으로 내려가며 탐색 
                    self.table[i] = [key,value] # 키가 동일하다면 값 변경 후 저장
                    return

    def get(self,key):
        index = self.hash(key)
        if self.table[index]==0:
            return None # 첫인덱스 조회시 데이터가 0이라면 데이터 존재하지 않음
        else:
            for i in range(index,self.max_len):
                if self.table[i][0]==index: #변환된 인덱스부터 밑으로 내려가며 탐색 
                    return self.table[i][1] # 키가 동일한 인덱스를 찾았다면 값 반환,
            return None # 동일한 인덱스 범위에 다른 값이 있지만 동일한 값을 찾지 못했다면 None 반환 








#hash Chaining 방법으로 만든 해시테이블 (list로 해시인덱스 데이터 저장)
class Chaining_Hash_table:
    def __init__(self,length= 97): # 97 테이블 크기만큼 나눈다
        self.max_len = length     #테이블 key를 97로 나누어 해싱
        self.table = [[] for __ in range(length)]

    def hash(self,key): #해시테이블에 key와 value넣기.
        hash_key = sum([ord(i) for i in key])
        return hash_key % self.max_len # #ord함수로 문자열 변경후 나온 값  % max_len

    def add(self,key,value):
        index = self.hash(key)
        self.table[index].append((key,value))

    def put(self,key,value):
        index = self.hash(key)
        if not value:         #리스트 안의 값이 존재하지않는다면 None반환
            return None
        for i in range(len(value)): # 리스트에서 동일한 값 찾기
            if value[i] == key:
                value.pop(i)  # pop으로 해시테이블 인덱스에 안에있는 튜플 제거
                break
        self.table[index].append((key,value)) # 수정할 데이터 추가,

    def get(self,key):
        index = self.hash(key)
        value = self.table[index]
        if not value:         #리스트 안의 값이 존재하지않는다면 None반환
            return None
        for v in value:       # 리스트에서 값을 찾아 반환 
            if v[0] == key:
                return v[1]
