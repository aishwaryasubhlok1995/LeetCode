class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        candidates = sorted(candidates)
        def backtrack(i, curr):
            if sum(curr) == target:
                final.append(curr.copy())
                return
            if sum(curr)>target or i == len(candidates):
                return 
            curr.append(candidates[i])
            backtrack(i+1, curr)
            curr.pop()
            while  i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr)
        backtrack(0, [])
        return final