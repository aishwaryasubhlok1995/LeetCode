# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return 
        quelist = deque()
        quelist.append(root)
        ans.append([root.val])
        while quelist:
            tempList = []
            for i in range(len(quelist)):
                node = quelist.popleft()
                if node.left != None:
                    tempList.append(node.left.val)
                    quelist.append(node.left)
                if node.right != None:
                    tempList.append(node.right.val)
                    quelist.append(node.right)
            if tempList:
                ans.append(tempList)
        return ans
        