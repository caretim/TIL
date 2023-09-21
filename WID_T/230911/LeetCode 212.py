class Node:
    def __init__(self):
        self.children={}
        self.endof =0

class Trie(object):
    def __init__(self):
        self.root = Node()
    def insert(self, word): # 노드 삽입, 딕셔너리로 존재하지않는다면 생성, 존재한다면 추가 
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = Node()
            node= node.children[i] 
        node.endof =1   # 완성문자열



class Solution(object):
    def findWords(self, board, words):
        result = []
        trie = Trie() # trieTree 생성
        node = trie.root
        for i in words: # 트라이트리에 단어 삽입
            trie.insert(i)
        for y in range(len(board)):
            for x in range(len(board[0])):
                self.search(node,board,y,x,"",result)


    def search(self,node,board,y,x,temp,result):
        dy,dx = [0,0,1,-1],[1,-1,0,0]
        if node.endof: # 현재 완성된 단어라면 tmep result에 추가 
            result.append(temp)
            node.endof = 0 #완성문자 방문체크
            if not node: 
                return
        if 0>y or y>=len(board) or 0>x or x>=len(board[0]): #범위체크
            return
        char = board[y][x]
        if char not in  node.children:
            return
        node = node.children[char]
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            self.search(node,board,ny,nx,temp+char,result)
            board[y][x]='*'
