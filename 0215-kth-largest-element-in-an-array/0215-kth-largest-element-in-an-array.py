class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        l = heapq.nlargest(k, nums)
        return l[-1]
        