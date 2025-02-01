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
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]
            if ptr == slow:
                return ptr
        return ptr
        

