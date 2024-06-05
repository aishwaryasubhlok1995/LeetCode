class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        ans = ''
        no = self.countAndSay(n-1)
        arr = [[no[0], 1]]
        if n >= 2:
            for i in range(1, len(no)):
                if arr[-1][0] == no[i]:
                    arr[-1][1] += 1
                else:
                    arr.append([no[i], 1])
            for i in range(len(arr)):
                ans +=  str(arr[i][1]) + str(arr[i][0]) 
            return ans
        return countAndSay(n-1)