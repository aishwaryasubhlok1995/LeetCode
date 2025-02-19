class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for i in strs:
            ans = [0]*26
            res = []
            for c in i:
                ans[ord(c) - ord("a")] += 1
            if tuple(ans) not in hm:
                hm[tuple(ans)] = [] 
            hm[tuple(ans)].append(i) 
        return hm.values()
            