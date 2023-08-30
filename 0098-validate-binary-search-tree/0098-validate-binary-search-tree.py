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
        minRange = -math.inf
        maxRange = math.inf
        def validate(root, minRange, maxRange):
            if root == None:
                return True
            if root.val >= maxRange or root.val <= minRange:
                return False
            return validate(root.left, minRange, root.val) and validate(root.right, root.val, maxRange)
        return validate(root, minRange, maxRange)
            