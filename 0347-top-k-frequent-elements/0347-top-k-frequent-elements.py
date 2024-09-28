class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        return heapq.nlargest(k,hm.keys(), key=hm.get)
            