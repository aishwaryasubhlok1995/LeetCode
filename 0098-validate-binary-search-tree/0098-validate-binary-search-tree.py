# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkLimits(self, root, minVal, maxVal):
        if root == None:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.checkLimits(root.left, minVal, root.val) and self.checkLimits(root.right, root.val, maxVal)
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal = -math.inf
        maxVal = math.inf
        if root == None:
            return 
        return self.checkLimits(root, minVal, maxVal)