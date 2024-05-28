class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            temp = nlargest(2, stones)
            if temp[0] != temp[1]:
                heapq.heappush(stones, temp[0]-temp[1])
            stones.remove(temp[0])
            stones.remove(temp[1])
        if len(stones) > 0:
            return stones[0]
        return 0