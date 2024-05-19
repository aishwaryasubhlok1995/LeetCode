class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            while start<end:
                sumOfNo = nums[start]+nums[end]+nums[i]
                if sumOfNo == 0:
                    ans.add((nums[i], nums[start], nums[end]))
                    start +=1
                    end -= 1
                elif sumOfNo < 0:
                    start += 1
                elif sumOfNo > 0:
                    end -= 1
        return ans 
        