class Solution:
  
    def mergeArray(self, nums1, nums2):
        ans = []
        i = 0 
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] > nums2[j]:
                    ans.append(nums2[j])
                    j += 1
                else:
                    ans.append(nums1[i])
                    i += 1
            elif i < len(nums1):
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        return ans 

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        middle = len(nums)//2
        leftHalf = nums[:middle]
        rightHalf = nums[middle::]
        leftArray = self.sortArray(leftHalf)
        rightArray = self.sortArray(rightHalf)
        return self.mergeArray(leftArray, rightArray)

    
