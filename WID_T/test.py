
import sys
class Solution(object):
    def __init__(self):
        self.prev = sys.maxsize
        self.current_min = sys.maxsize
        def getMinimumDifference(self, root):
            def findMin(node):
                if node != None:
                    return 
                findMin(node.left)
                self.result = min(abs(node.val-self.prev),self.result)
                self.prev = node

                findMin(node.right)


            findMin(root)
            return self.result

