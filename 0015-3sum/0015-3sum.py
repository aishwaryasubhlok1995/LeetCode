class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tempSet = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            valToSearch = nums[i]*-1
            left = i+1
            right = len(nums) - 1
            while left<right:
                if nums[left] + nums[right] == valToSearch:
                    if (nums[left], nums[right], valToSearch*-1) not in tempSet:
                        tempSet.add((nums[left], nums[right], valToSearch*-1))
                        '''resArray.append([nums[left], nums[right], valToSearch*-1])'''
                    left += 1
                elif nums[left] + nums[right] < valToSearch:
                    left += 1
                else:
                    right -= 1
            
        return list(tempSet)
