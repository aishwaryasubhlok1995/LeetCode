import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = heapq.nlargest(k, nums)
        print(res)
        return res[-1]
        