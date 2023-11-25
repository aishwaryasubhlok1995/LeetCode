# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkMirror(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            if root1.val != root2.val:
                return False
            else:
                return checkMirror(root1.left, root2.right) and checkMirror(root1.right, root2.left)
        if root == None or (root.left == None and root.right == None):
            return True
        if root.left != None and root.right != None:
            return checkMirror(root.left, root.right)
       
           
        
        