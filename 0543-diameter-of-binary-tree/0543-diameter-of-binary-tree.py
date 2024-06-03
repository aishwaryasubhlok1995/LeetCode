# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #find height of binary tree
        maximumValue = 0
        def findHeight(node):
            nonlocal maximumValue
            if node == None:
                return 0
            left = findHeight(node.left)
            right = findHeight(node.right)
            maximumValue = max(maximumValue, (left+right))
            return max(left, right)+1
        findHeight(root)
        return maximumValue
                
        