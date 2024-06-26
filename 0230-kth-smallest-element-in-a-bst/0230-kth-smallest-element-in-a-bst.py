# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import heapq
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def findKElement(root):
            nonlocal arr
            if root == None:
                return 
            if root.left:
                findKElement(root.left)
            arr.append(root.val)
            if root.right:
                findKElement(root.right)
        findKElement(root)
        return arr[k-1]
            
        
        
        
        
        
        
        
        