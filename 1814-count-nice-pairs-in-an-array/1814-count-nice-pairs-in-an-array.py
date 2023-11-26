class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        key = math.inf
        res = 0
        dict = {}
        #Reverse
        def reverse(rem, num):
            while num > 0:
                rem = rem*10 + num%10
                num = num//10
            return rem
        
        for i in range(len(nums)):
            x = nums[i] - reverse(0, nums[i])
            if x in dict.keys():
                dict[x] += 1
            else:
                dict[x] = 1
        print(dict)
        for i in dict.values():
            if i>1:
                res += (i*(i-1))//2
            
        return res % (pow(10,9) + 7)