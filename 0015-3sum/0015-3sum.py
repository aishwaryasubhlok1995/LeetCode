class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()

        for k in range(len(nums)):
            x = -1 * nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == x:
                    ans.add((nums[i], nums[j], nums[k]))
                    i += 1
                else:
                    if nums[i] + nums[j] < x:
                        i += 1
                    else:
                        j -= 1
        print(ans)
        return ans
        