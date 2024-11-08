# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLengthOfLinkedList(headA, count):
            curr = headA
            while curr != None:
                count += 1
                curr = curr.next 
            return count
        lenheadA = getLengthOfLinkedList(headA, 0)
        lenheadB = getLengthOfLinkedList(headB, 0)
        value = abs(lenheadA - lenheadB)
        if lenheadA > lenheadB:
            curr = headA
            curr1 = headB
        else:
            curr = headB
            curr1 = headA
        count = 0 
        while count != value:
            curr = curr.next 
            count += 1
        while curr != curr1:
            curr = curr.next 
            curr1 = curr1.next
        if curr == curr:
            return curr 
        return None 
        
            
            