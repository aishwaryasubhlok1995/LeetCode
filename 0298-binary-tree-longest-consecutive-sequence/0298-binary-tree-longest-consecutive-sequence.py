# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateMaxLength(self, prev, curr, length):
        if curr == None:
            return 1
        else:
            if curr.val - prev  == 1:
                length = length + 1
            else:
                length = 1
        return max(length, self.calculateMaxLength(curr.val, curr.left, length), self.calculateMaxLength(curr.val, curr.right, length))
   
    def longestConsecutive(self, root: Optional[TreeNode]) -> int: 
        maxLength = 1
        return max((self.calculateMaxLength(root.val, root.left, maxLength)), (self.calculateMaxLength(root.val, root.right, maxLength)))
                 
        
    
            
        
        