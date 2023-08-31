# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        maxRange = math.inf
        minRange = -math.inf
        def validateBinaryTree(root, minRange, maxRange):
            if root == None:
                return True
            if root.val <= minRange or root.val >= maxRange:
                return False
            return validateBinaryTree(root.left, minRange, root.val) and validateBinaryTree(root.right, root.val, maxRange)
        
        return validateBinaryTree(root, minRange, maxRange)
       
            
            
                