# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateLeafLeftNode(self, root, finalList):
        if root.left ==  None and root.right == None:
             finalList.append(root.val)
        else:
            if root.left != None:
                self.calculateLeafLeftNode(root.left, finalList)
            if root.right != None:
                self.calculateLeafLeftNode(root.right, finalList)
            
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        finalList = []
        self.calculateLeafLeftNode(root1, finalList)
        print(finalList)
        finalList1 = finalList
        finalList = []
        self.calculateLeafLeftNode(root2, finalList)
        print(finalList1)
        return True if finalList1 == finalList else False
            
        