class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        ptr = nums[0]
        while 1:
            slow = nums[slow]
            fast  = nums[nums[fast]]
            if slow == fast:
                break
        print(slow)
        while 1:
            if ptr == slow:
                break
            ptr = nums[ptr]
            slow = nums[slow]
        return ptr
        

