class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = [1]*(len(nums))
        for i in range(len(nums)):
            arr = []
            for j in range(0, i):
                if nums[j] < nums[i]:
                    arr.append(sequence[j])
            if len(arr) > 0:
                sequence[i] = 1 + max(arr)
        return max(sequence)

        