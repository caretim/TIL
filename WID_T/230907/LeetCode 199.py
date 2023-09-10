# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        self.result = []
        self.level = 0
        self.findRight(root,0)
        return self.result
    
    def findRight(self, node,level):
        if node == None:
            return
        if len(self.result) == self.level:
            self.result.append(node.val)
        self.findRight(node.right,level+1)
        self.findRight(node.left,level+1)
        

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        