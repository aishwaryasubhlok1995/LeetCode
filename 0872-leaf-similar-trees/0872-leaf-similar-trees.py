# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateLeafLeftNode(self, root, finalList):
        if root == None:
            return
        if root.left ==  None and root.right == None:
             finalList.append(root.val)
        else:
            self.calculateLeafLeftNode(root.left, finalList)
            self.calculateLeafLeftNode(root.right, finalList)
            
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = [], []
        self.calculateLeafLeftNode(root1, leaf1)
        self.calculateLeafLeftNode(root2, leaf2)
        return leaf1 == leaf2 
            
        