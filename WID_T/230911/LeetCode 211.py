class Node:
    def __init__(self):
        self.children={}
        self.endof =False


class WordDictionary(object):

    def __init__(self):
        self.root = Node()

        

    def addWord(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = Node()
            node= node.children[i] 
        node.endof =1   # 완성문자열
        
    def dictFind(self,node,word):
        if not word: # 마지막 도달 종료 조건 
            if node.endof:
                self.result = True
            return 
        if  word[0] == '.':
            for i in node.children.values():
                self.dictFind(i,word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dictFind(node,word[1:])



    def search(self, word):
        node = self.root
        self.result = False
        self.dictFind(node,word)
        return self.result
        

        """
        :type word: str
        :rtype: bool
        """
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)