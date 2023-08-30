class Node:
    def __init__(self,data): 
        self.data = data # 노드값 
        self.next = None # 최초 생성시 다음 노드 지정안함

class LinkedList:
    def __init__(self,data): # 최초 링크드리스트 사용시 헤더 생성
        self.head = Node(data)

    def append(self,data):
        cur = self.head  # 현재 리스트의 헤드(시작점) 찾기
        while cur.next is not None: # 마지막 다음 목적지가 NOne값이 나올떄까지 반복
            cur= cur.next
        cur.next = Node(data) # 마지막 노드와 현재 추가하려는 노드 연결 

    def find_index(self,data):  #값으로 인덱스 찾기
        now =self.head # 헤드부터 시작해서 data값과 동일한 값 찾기 
        cnt=0
        while now == data:  # 동일한값을 찾는ㄴ다면 정지 
            if now.data ==data:
                break
            cnt+=1
            now = now.next
        print(cnt)
    def get_node(self,data): #인덱스 노드 위치 찾기
        now = self.head #리스트의 헤드 찾기
        cnt =0
        while now>data:
            now =now.next
            cnt+=1
        return cnt
    def insert_node(self,index,data): #노드 삽입
        new_node = Node(data)
        if index==0:  # 헤드변경 
            new_node.next = self.head
            self.head = new_node
            return
        find_node= self.get_node(index-1) # 찾을 인덱스의 전 인덱스 찾기 
        new_node.next =  find_node.next # 생성된 노드의 next를 전 인덱스의 next로 변경
        find_node.next = new_node # 찾은 인덱스 -1 의 next를 생성된 노드로 지정 
        
    def delete_node(self,index):
        if index ==0:
            self.head = self.head.next
            return
        find_node =self.get_node(index-1) # 인덱스-1 를 찾은 후 현재 인덱스의 앞의 연결된 부분을 연결
        find_node.next = find_node.next.next # 인덱스 next변경해줌 




        


        
        
                 
                