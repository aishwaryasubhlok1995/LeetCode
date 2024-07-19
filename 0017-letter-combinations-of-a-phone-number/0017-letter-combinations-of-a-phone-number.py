class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {'2':'abc', '3':'def', '4':'ghi','5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        if digits == "":
            return ans
        def backtracking(i, curr):
            if i == len(digits):
                var = ''
                for i in curr:
                    var += i
                ans.append(var)
                return
            if digits[i] in hm and i<len(digits):
                x = hm[digits[i]]
            for char in range(len(x)):
                curr.append(x[char])
                backtracking(i+1, curr)
                curr.pop()
        backtracking(0, [])
        return ans
        
        
        