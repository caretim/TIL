class Node:
    def __init__(self,data): 
        self.data = data # 노드값 
        self.next = None # 최초 생성시 다음 노드 지정안함
        self.min = None
        self.prev = None

class MinStack(object):
    def __init__(self):
        self.head =None #스택 생성시 시작부분 설정 (아직 값이 없기에 None)
        self.tail = None

    def push(self, val):
        node = Node(val)
        node.min = val
        if self.head == None:
            node.min= val
            self.head = node
            self.tail = node
            return
        node.min = min(self.tail.min,val) #최소값 노드에 저장 
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        
        

    def pop(self):
        if self.tail.prev ==None: # 스택의 마지막 인자 (prev = None일 경우 스택의 헤드 초기화)
            self.head =None
            return
        self.tail = self.tail.prev
         #마지막 head =None  #tail값을 tail.prev로 변경
        # self.tail.next = None # 변경된 tail의 next None으로 지정

        """
        :rtype: None
        """
        

    def top(self):
        return self.tail.data
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.tail.min
        


