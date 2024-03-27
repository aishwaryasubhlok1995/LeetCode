# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateHeight(self, root):
        if root == None:
            return 0
        else:
            return max(self.calculateHeight(root.left), self.calculateHeight(root.right)) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True 
        else:
            if abs(self.calculateHeight(root.left) - self.calculateHeight(root.right))>1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
           
            
        
     
        