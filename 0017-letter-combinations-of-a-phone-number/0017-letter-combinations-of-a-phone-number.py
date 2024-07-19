class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {'2':'abc', '3':'def', '4':'ghi','5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        if digits == "":
            return ans
        def backtracking(i, curr):
            if i == len(digits):
                ans.append(curr[:])
                return
            if digits[i] in hm and i<len(digits):
                x = hm[digits[i]]
            for char in range(len(x)):
                curr += (x[char])
                backtracking(i+1, curr)
                curr = curr[:-1]
        backtracking(0, "")
        return ans
        
        
        