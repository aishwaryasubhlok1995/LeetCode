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
        while quelist:
            tempList = []
            for i in range(len(quelist)):
                node = quelist.popleft()
                tempList.append(node.val)
                if node.left:
                    quelist.append(node.left)
                if node.right:
                    quelist.append(node.right)
            ans.append(tempList)
        return ans
        