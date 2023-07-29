class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in range(len(strs)):
            res = []
            sortedString = ''.join(sorted(strs[i]))
            if sortedString in dict.keys():
                res = dict.get(sortedString)
            else:
                dict[sortedString] = res
            res.append((strs[i]))
        return dict.values()
            