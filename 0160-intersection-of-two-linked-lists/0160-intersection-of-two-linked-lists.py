# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setIntersectVal = set()
        curr = headA
        curr2 = headB
        while curr != None:
            setIntersectVal.add(curr)
            curr = curr.next 
        while curr2 != None:
            if curr2 in setIntersectVal:
                return curr2
            curr2 = curr2.next 
        return None
        
            
            