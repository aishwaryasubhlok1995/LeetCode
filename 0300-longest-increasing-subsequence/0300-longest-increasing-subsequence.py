class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = [1]*(len(nums))
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    sequence[i] = max(sequence[i], 1+sequence[j])
        return max(sequence)

        