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
        while curr.next != None:
            curr = curr.next 
            counter += 1
        curr.next = head
        k = k % counter
        counter = counter-k
        curr = head
        for i in range(counter-1):
            curr = curr.next 
        head = curr.next 
        curr.next = None   
        return head
        
            
            
            
        