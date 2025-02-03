class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        curr = []
        nums = sorted(nums)
        def subset(i):
            if i == len(nums):
                final.append(curr.copy())
                return
            curr.append(nums[i])
            subset(i+1)
            curr.pop()
            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            subset(i+1)
        subset(0)
        return final

        