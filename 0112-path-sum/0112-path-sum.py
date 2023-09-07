# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        totalSum = 0
        def calculateSum(root, totalSum):
            if root == None:
                return False
            if root.left == None and root.right == None:
                if targetSum == totalSum + root.val:
                    return True
                return False
            else:
                totalSum  += root.val
            return calculateSum(root.left, totalSum) or calculateSum(root.right, totalSum)
        return calculateSum(root, totalSum)

        
        
        