class Solution(object):
    def averageOfLevels(self, root):
        self.depth = 0	#깊이 체크 포인터
        self.result=[]	# 레벨별로 값이 담길 리스트
        self.count =[]	# 레벨별로 개수가 담길 리스트
        self.find(root,0) # 시작
        for i in range(len(self.result)):	# 구해진 값들을 result(레벨별 총합)/count(레벨별 개수)
            self.result[i]= float(self.result[i])/float(self.count[i])
         
    
        return self.result # 나눠진 값이 담긴 리스트 리턴 
            
    def find(self,node,depth):
        if node== None:	# node가 비었다면 return 
            return
        if len(self.result)==depth: # 깊이와 레벨이 같다면 각 리스트의 길이 추가
            self.result.append(node.val)
            self.count.append(1)
        else:
            self.result[depth]+=node.val # 다르다면 레벨에 맞게 result와 count에 값 추가
            self.count[depth]+=1
        self.find(node.left,depth+1) #재귀적으로 left,right 탐색 
        self.find(node.right,depth+1)