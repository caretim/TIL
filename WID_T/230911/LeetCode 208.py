class Node:
    def __init__(self):
        self.children={}
        self.endof =False

class Trie(object):
    def __init__(self):
        self.root = Node()
        self.root.endof =False
        

    def insert(self, word): # 노드 삽입, 딕셔너리로 존재하지않는다면 생성, 존재한다면 추가 
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = node[i]
            node= node.children[i] 
        node.endof =1   # 완성문자열
            
    def search(self, word):
        cur = self.root
        for i in word: # 트라이트리하위에 글자가 존재하지 않는다면
            if i not in cur.children:
                return False
            cur = cur.children[i]
        if cur.endof ==1:
            return True


    def startsWith(self, prefix):
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)