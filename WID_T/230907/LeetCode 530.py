class Solution:
    def getMinimumDifference(self, root) :
        self.prev = float('-inf')
        self.res = float('inf')
        
        def findMin(node):
            if node is None:
                return
                                        
            findMin(node.left)
            
            self.res = min(node.val - self.prev, self.res)
            self.prev = node.val

            findMin(node.right)
        
        findMin(root)
        return self.res

