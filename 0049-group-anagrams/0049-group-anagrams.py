class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in range(len(strs)):
            res = []
            if ''.join(sorted(strs[i])) in dict.keys():
                res = dict.get(''.join(sorted(strs[i])))
                res.append(strs[i])
            else:
                dict[''.join(sorted(strs[i]))] = res
                res.append((strs[i]))
        print(dict.values())
        return dict.values()
            