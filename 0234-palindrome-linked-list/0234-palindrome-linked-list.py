# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       
        curr = head
        temp = [curr.val]
        while curr.next != None:
            curr = curr.next
            temp.append(curr.val)
        if temp == temp[::-1]:
            return True
        return False
            
     

        
        