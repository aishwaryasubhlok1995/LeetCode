# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = [root]
        res = []
        result=[]
        if root == None:
            return []
        while len(q) != 0:
            arr = []
            for i in range(len(q)):
                node = q.pop(0)
                if node.left != None:
                    q.append(node.left )
                    #arr.append(node.left.val)
                if node.right != None:
                    q.append(node.right)
                arr.append(node.val)
            result.append(arr)
            
                   
        return(result)
            
        