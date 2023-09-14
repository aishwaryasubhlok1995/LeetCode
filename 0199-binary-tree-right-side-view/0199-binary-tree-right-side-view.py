# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        res = []
        if root == None:
            return None
        arr.append(root) 
        res.append(root.val)
        while len(arr) != 0:
            lenArr = len(arr)
            for i in range(lenArr):
                if arr[i].left != None:
                    arr.append(arr[i].left)
                if arr[i].right != None:
                    arr.append(arr[i].right)
            arr = arr[lenArr::]
            if len(arr) > 0:
                res.append(arr[-1].val)
        print(res)
        return res
        