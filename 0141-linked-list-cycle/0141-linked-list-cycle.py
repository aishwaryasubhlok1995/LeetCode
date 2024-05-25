# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setNodes = set()
        curr = head
        setNodes.add(curr)
        while curr != None:
            curr = curr.next
            if curr not in setNodes:
                setNodes.add(curr)
            else:
                return True
        return False