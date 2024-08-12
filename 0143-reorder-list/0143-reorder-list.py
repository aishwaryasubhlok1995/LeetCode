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
        while fast!= None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
            
        #rev logic
        curr = slow.next 
        slow.next = None
        prev = None
        while curr != None:
            next = curr.next 
            curr.next = prev
            prev = curr 
            curr = next
        head1=prev
        head2 = head
        while head1:
            temp = head2.next 
            head2.next = head1
            head2 = temp 
            
            temp = head1.next 
            head1.next = head2
            head1 = temp
        return head
            
    
       
                
                
            
            
            