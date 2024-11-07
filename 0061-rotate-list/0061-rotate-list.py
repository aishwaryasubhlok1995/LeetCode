# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return 
        curr = head
        counter = 1
        noOfNodes = 0
        while curr.next != None:
            curr = curr.next 
            counter += 1
        noOfNodes = counter
        if k < counter:
            counter = counter - k 
        else: 
            no = k % counter 
            counter = counter - no
        if k == 0 or noOfNodes == counter:
            return head
        curr = head
        count = 1
        while count != counter: 
            curr = curr.next 
            count += 1
        temp = curr.next  
        head1 = temp
        curr.next = None 
        curr = head1
        while curr != None and curr.next != None:
            curr = curr.next 
        if curr != None:
            curr.next = head
        return head1
        
            
            
            
        