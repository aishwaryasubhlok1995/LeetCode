class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1
        final = heapq.nlargest(k, hm.keys(), key = hm.get)
        return final