class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        maxSum = 0
        sumOfNo = 0
        setNums = set()
        while i <= len(nums)-k and j < len(nums):
            if nums[j] not in setNums and len(setNums) < k:
                setNums.add(nums[j])
                sumOfNo += nums[j]
                if len(setNums) == k:
                    maxSum = max(maxSum, sumOfNo)
                j += 1
            else:
                setNums.remove(nums[i])
                sumOfNo -= nums[i]
                i += 1
        return maxSum
        