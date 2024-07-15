class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        def backTrack(pendingElement, curr):
            if len(pendingElement) == 1:
                curr.append(pendingElement[0])
                final.append(curr[:])
                curr.pop()
                return 
            for i in range(len(pendingElement)):
                curr.append(pendingElement[i])
                backTrack(pendingElement[:i] + pendingElement[i+1:], curr)
                curr.pop()
        backTrack(nums, [])
        return final

        