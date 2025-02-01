# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head 
        fast = head 
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next 
        curr = slow.next 
        prev = None
        slow.next = None
        while curr:
            Next = curr.next 
            curr.next = prev 
            prev = curr
            curr = Next 
        h2 = prev 
        h1 = head 
        while h2:
            temp = h1.next
            h1.next = h2
            h1 = h2
            h2 = temp 

           
        
        
        