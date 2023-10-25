"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        maxRes = 0
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        if root.children == []:
            return 1
        else:
            for i in range(len(root.children)):
                curMax = self.maxDepth(root.children[i])+1
                maxRes = max(curMax, maxRes)
        return maxRes

