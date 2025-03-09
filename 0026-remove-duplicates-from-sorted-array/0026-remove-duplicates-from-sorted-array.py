class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        uniqueNos = set()
        uniqueNos.add(nums[0])
        i = 1
        while i<len(nums) and j<len(nums):
            if nums[i] not in uniqueNos:
                uniqueNos.add(nums[i])
                i += 1
            elif nums[j] in uniqueNos:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                uniqueNos.add(nums[i])
                i += 1
                j += 1
        return len(uniqueNos)
