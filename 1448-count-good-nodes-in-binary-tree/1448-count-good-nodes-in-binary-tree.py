# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def countGoodNodes(root, newMax):
            nonlocal count 
            if root == None:
                return count
            if root.val >= newMax:
                count += 1
                newMax = root.val
            countGoodNodes(root.left, newMax)
            countGoodNodes(root.right, newMax)
            return count

        return countGoodNodes(root, root.val)
            
        