# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val != q.val:
            return False
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        if self.isSameTree(root, subRoot) == True:
            return True
        else:
            if root.left != None:
                if self.isSubtree(root.left, subRoot) == True:
                    return True
            if root.right != None:
                 if self.isSubtree(root.right, subRoot) == True:
                    return True
                

            

