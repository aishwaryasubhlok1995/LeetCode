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
        heapq.heapify(arr)
        def findKElement(root, k):
            nonlocal arr
            if root == None:
                return arr
            if len(arr) < k:
                heapq.heappush(arr, -root.val)
            else:
                if arr[0] < -root.val:
                    heapq.heappop(arr)
                    heapq.heappush(arr, -root.val)
            findKElement(root.left, k)
            findKElement(root.right, k)
            return arr[0]
                    
        return -1*findKElement(root, k)
        
        
        
        