# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
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
        curr = head
        Next = head1
        while Next!= None:
            temp = curr.next
            curr.next = Next
            curr = Next
            Next = temp
           
            

            
            
            
            
            
        
        