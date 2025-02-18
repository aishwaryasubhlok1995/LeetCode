class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0 
        j = 1 
        numsSet = set()
        numsSet.add(nums[i])
        while j < len(nums):
            if j - i <= k:
                if nums[j] in numsSet:
                    return True 
                numsSet.add(nums[j])
                j += 1
            else:
                numsSet.remove(nums[i])
                i += 1
        return False


        